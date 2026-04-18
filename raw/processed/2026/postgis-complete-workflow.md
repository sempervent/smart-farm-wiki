If you have separate shapefiles for world countries and major cities, you can view and query the data using ArcGIS, QGIS, or any other GIS software package. You can download the data from [here](https://drive.google.com/file/d/1HhyQ1b7wDoripkCfBrG7qSYKO3MMNO2g/view?usp=sharing) (made with Natural Earth).

For instance, you can perform the following operations:

- Use the *identify* tool to get some information about the feature you clicked
- Determine or set which Spatial Reference System the data is referring to
- Reproject your data
- Compute distance and area
- Compute centroid
- Perform buffer analysis

**The good news** is that you can do all these operations with PostGIS. A question may arise on the necessity of performing all these operations on a spatial database. What’s the point of reformulating our problem in PostGIS when we can do it easily in an open-source or proprietary software package?

PostGIS would come in handy when you want to develop your web, mobile, or desktop app. The data we are using here consists of just a limited number of static records. In some cases, you may find yourself in a situation where there is a continuous data flow. Desktop GIS tools may not be appropriate to digest this kind of data and perform (near) real-time analysis.

When dealing with a geospatial problem, there are four significant steps you can consider to answer the question correctly:

1. [Modelling](#48b9)
2. [Preparation and loading the data](#d67c)
3. [Write a query to solve the problem](https://medium.com/@fashouri/8dc2732bbde8#b37b)
4. [View the results](https://medium.com/@fashouri/8dc2732bbde8#cac4)

I depicted the steps on a diagram for you:

![Figure 1 - Spatial problems workflow for spatial databases (image by Author)](https://towardsdatascience.com/wp-content/uploads/2021/10/1Vp62jjtvqUxUq0tKoY6yvA.png)

Figure 1 – Spatial problems workflow for spatial databases (image by Author)

We will go through all these steps and try to tackle the challenges proposed earlier.

## 1\. Modelling

Modelling is the process of translating the real world into a model that is composed of database objects. In other words, a model, by definition, is the simplified representation of reality. For example, you’ll represent the countries as polygons and cities as points. You’ll then create a table for each. You need to store some information about each record. You may not be able to keep all the information about them, so you’ll choose the ones that help you with the problem at hand or problems that may arise later.

At the first step, you need to create a database and a schema to hold your data. A schema is a container that logically segments objects (tables, functions, views, and so on) for better management. There is a default public schema in the database you create in PostgreSQL, but I’d instead create a new one. Keep in mind that it is up to you to what extent you want to simplify the real world in your model. Modelling is inherently a tradeoff between simplicity and adequacy. Even though all models have flaws, they provide us with a more cost-effective approach. It would be best if you created a database and a schema first:

```
CREATE DATABASE postgis_training;
 CREATE SCHEMA postgis1;
```

PostGIS functions and operations would not work by default, and you need to enable PostGIS in your database to make them work:

```
CREATE EXTENSION postgis;
```

We need to create two tables to house world countries and cities data:

```
CREATE TABLE postgis1.countries (
  id serial,
  formal_name VARCHAR(50) PRIMARY key,
  country_iso3 CHAR(3),
  population INT,
  gdp INT,
  economy VARCHAR(50),
  income_group VARCHAR(50),
  continent VARCHAR(50),
  subregion VARCHAR(50),
  region_world_bank VARCHAR(50),
  geog geography(multipolygon, 4326)
);
```
```
CREATE TABLE postgis1.cities (
  id SERIAL PRIMARY KEY,
  city_name VARCHAR(50),
  country_iso3_code CHAR(3),
  featurecla VARCHAR(50),
  population INT,
  geog GEOGRAPHY(POINT, 4326)
);
```

Take a look at shapefiles that you have already [downloaded](https://drive.google.com/file/d/1HhyQ1b7wDoripkCfBrG7qSYKO3MMNO2g/view?usp=sharing). We do not need all the fields that they have provided. We choose the ones that are appropriate for our problem. I think the column names in the tables we created are intuitive enough, and there is no need for any explanations except for just a few of them. Columns \_country *iso3* and \_country\_iso *code* here denote Alpha-3 codes, which are three-letter country codes defined in *ISO 3166–1* published by the *International Organization for Standardization (ISO)*. I intentionally have chosen different names here to avoid confusion. You can use the same names for columns that have the same meaning.

You can see the ERD representation of our database in Figure 2. For those of you who may not be familiar with the \_spatial\_ref *sys* table, it is a table in every PostGIS enabled database that lists all the valid SRID values and their corresponding *proj4text* representation of a Spatial Reference System (SRS).

![Figure 2 - ERD representation of the database (image by Author)](https://towardsdatascience.com/wp-content/uploads/2021/10/1yOdERw730CeDQFVIbJ_bgA.png)

Figure 2 – ERD representation of the database (image by Author)

## 2\. Preparation and loading the data

Let’s import all your shapefiles as it is directly into our database. When we import data directly from an external file, we normally call it a staging table. A staging table is just a temporary table containing the raw data. They are used to populate the main tables in the model we already designed. To import the \_ne\_50m\_populated *places.shp* shapefile, we use a command-line utility called *shp2pgsql* that come with PostGIS installation. Navigate to your shapefiles folder in the command-line tool of your operating system and run the following command:

```
shp2pgsql -s 4326 -I -G ne_50m_populated_places.shp postgis1.cities_staging > staging_cities.sql
```

It would create a file called \_staging *cities.sql* in the same folder. We are telling that the SRID of the table we want to create is 4326 (*\-s 4326*). We Create a spatial index on the geocolumn by adding *\-I* as an option. We add *\-G* option which means we are using the geography type. You can do much more with this command, but we decided to keep things simple here. The next step is to run created SQL file to make the \_postgis1.cities *staging* table. You can use the built-in *psql* command-line utility to do that:

```
psql -h localhost -d postgis_training -U postgres -f staging_cities.sql
```

Do the same for the \_ne\_110m\_admin\_0 *countries.shp* table with the following commands:

```
shp2pgsql -s 4326 -I -G ne_110m_admin_0_countries.shp postgis1.countries_staging > staging_countries.sql
```
```
psql -h localhost -d postgis_training -U postgres -f staging_countries.sql
```

Now that we have imported our shapefiles, it is about time to populate the tables we created in our model.

```
INSERT INTO postgis1.countries (
  formal_name, country_iso3, population, gdp,
  economy, income_group, continent, subregion,
  region_world_bank, geog
)
SELECT
  name_sort,
  adm0_a3,
  pop_est,
  gdp_md_est,
  economy,
  income_grp,
  continent,
  subregion,
  region_wb,
  geog
FROM 
  postgis1.countries_staging;
```
```
INSERT INTO postgis1.cities (
  city_name, country_iso3_code, featurecla,
  population, geog
)
SELECT 
  NAME,
  SOV_a3,
  FEATURECLA,
  POP_OTHER,
  geog
FROM 
  postgis1.cities_staging;
```

We just selected the corresponding columns from staging tables to populate our main tables.

We have covered how to model a spatial problem and populate it with real-world data. In the next section of this article, we will deal with some common questions that you may come up with.

## 3\. Write a query to solve the problem

Now our model and database are ready to run spatial SQL queries to answer different questions. Here we have some questions to answer, and we will go through each of them:

**Select and create a table of all European countries**

As an ice-breaker, we would like to return European countries. We don’t use any spatial functions here:

```
SELECT 
  * INTO postgis1.eu_countries
FROM 
  postgis1.countries
WHERE 
  continent = 'Europe'
```

**Select all the cities that reside inside European countries**

Now we select all the cities that intersect with European countries. Since we need both tables, we have to join the tables:

```
SELECT 
  postgis1.cities.* INTO postgis1.eu_cities
FROM 
  postgis1.cities
  INNER JOIN postgis1.eu_countries ON
    ST_Intersects(
      postgis1.cities.geog, postgis1.eu_countries.geog
    );
```

**Reproject European cities and countries tables and store them as separate geometry tables**

If you want to reproject a geography table into a projected coordinate reference system, you convert the geography column into a geometry column. Then the geog column name may be misleading. At first, let’s rename the geog column in both tables into *geom*:

```
ALTER TABLE 
  postgis1.eu_cities RENAME COLUMN geog TO geom;
```
```
ALTER TABLE 
  postgis1.eu_countries RENAME COLUMN geog TO geom;
```

Notice that we renamed our columns to geom, but they still inherently contain geography data. We don’t let this situation last any longer and transform it into World Mercator (SRID 3395) which is a projected coordinate reference system:

```
ALTER TABLE 
  postgis1.eu_cities ALTER COLUMN geom TYPE geometry(POINT, 3395)
  USING ST_Transform(geom::geometry, 3395);
```
```
ALTER TABLE 
  postgis1.eu_countries ALTER COLUMN geom TYPE
  geometry(MULTIPOLYGON, 3395) USING ST_Transform(geom::geometry,
  3395);
```

Now we have fully transformed our European tables into World Mercator and geometry data type. Many PostGIS functions do not support geography type. Besides, many spatial calculations are inherently performed correctly on a projected CRS. We consider these two tables for the rest of the operations.

**Export newly created tables as shapefiles**

You can make use of another command-line utility called *pgsql2shp* to export spatial tables to shapefiles. Run the following commands in the command-line tool available on your operating system. Make sure to make a folder called *shp* in the same folder you are running the commands:

```
pgsql2shp -f ./shp/eu_cities_shp -h localhost -u postgres postgis_training postgis1.eu_cities
```
```
pgsql2shp -f eu_countries_shp -h localhost -u postgres postgis_training postgis1.eu_countries
```

The commands will create shapefiles of cities and countries in the *shp* folder.

The format of the *pgsql2shp* command is as follows:

```
pgsql2shp [options] database [schema.]table
```

The options seem intuitive enough, but I elaborate on them to make everything clear:

```
-f use this option to specify the shapefile name and address you want to create
```
```
-h use this option to specify the database host to connect to
```
```
-u use this option to connect to the database as the specified user
```

You might want to consider some other options, but the specified options are enough for what we want to do.

**Identify the country that a particular point is located**

Consider having coordinates in a geodetic coordinate system (WGS84 lon/lat SRID of 4326) in which longitude = 32.6542 and latitude = 50.9533. We want to know which country this point lies in. What we want to do is comparable to *identify* tool in most GIS software packages.

Notice that our dataset no longer uses the SRID of 4326. We need to transform the point into World Mercator (SRID 3395) on the fly:

```
WITH identify AS(
  SELECT 
    ST_Transform(
      ST_SetSRID(
        ST_Point(32.6542, 50.9533),
        4326
      ),
      3395
    ) AS ipoint
)
```
```
SELECT 
  postgis1.eu_countries.*
FROM
  postgis1.eu_countries,
  identify
WHERE
  ST_Within(ipoint, geom)
```

We used a CTE to define and transform a point. \_ST *Within(geometry A, geometry B)* returns TRUE if geometry A is entirely inside geometry B. This function will help us find the country we are looking for.

**Find the area of a country**

PostGIS has a \_ST *Area* function that is used to determine the area of a polygon. It returns the area with units specified by the SRID. Once more, we need to transform the SRID on the fly:

```
WITH identify AS(
  SELECT 
    ST_Transform(
      ST_SetSRID(
        ST_Point(32.6542, 50.9533),
        4326
      ),
      3395
    ) AS ipoint
)
```
```
SELECT 
  ST_Area(geom)
FROM
  postgis1.eu_countries,
  identify
WHERE
  ST_Within(ipoint, geom)
```

The identify CTE part is just for finding the country, followed by a piece of code to determine the area. If we run this code, it returns 1394397442159.71, and the unit is in square meters, equivalent to 1394.39 square kilometres. If you google the size of Ukraine, you get quite a different figure. The area of Ukraine is 603.63 square kilometres. We computed a figure that is over two times the actual figure. How can this be justified?

The fact of the matter is that World Mercator (SRID 3395) does not preserve the area. From the equator outward, the area of polygons rises much faster than the actual number. That’s why Greenland looks much larger on many world maps. To get an accurate area, we need to use an equal-area Spatial Reference System. I chose Europe Albers Equal Area Conic (SRID 102013) for that. It covers the whole of Europe and hopefully preserves the area of polygons. We need an on-the-fly transformation of Ukrain polygon in our query:

```
WITH identify AS(
  SELECT
    ST_Transform(
      ST_SetSRID(
        ST_Point(32.6542, 50.9533),
        4326
      ),
      3395
    ) AS ipoint
)
SELECT
  ST_Area(
    ST_Transform(geom, 3035)
  )
FROM 
  postgis1.eu_countries,
  identify
WHERE 
  ST_Within(ipoint, geom)
```

The result is 601914411764.12 square meters is equivalent to 601.91 square kilometres. It is comparable to the official area of the country (603.63 km2), and the slight difference is most likely due to inaccurate polygons on the map.

Still, there is a second option. The area and distance measurements (especially over the large areas) are guaranteed to be accurate when using the geography type. Moreover, the curvature of the earth is considered. To take advantage of geography type, let’s look at the *countries* table in our original model and see if we can solve the problem. Nevertheless, not all spatial functions, including \_ST *Distance* are supported by geography type. We can opt for \_ST *Covers* that works well with geography type:

```
WITH identify AS(
  SELECT
    ST_SetSRID(
      ST_Point(32.6542, 50.9533),
      4326
    ) AS ipoint
)
SELECT 
  ST_Area(geog)
FROM 
  postgis1.countries,
  identify
WHERE 
  ST_Covers(geog, ipoint)
```

**Find the distance between Berlin and London.**

We have learned from the previous challenge that for measurements over large areas, geography data type might be a suitable option:

```
SELECT 
  ST_Distance(a.geog, b.geog)
From 
  postgis1.cities a,
  postgis1.cities b
WHERE 
 a.city_name = 'Berlin'
 AND b.city_name = 'London'
```

Since you want to find the distance between two points in the same table, you must reference the same table twice. \_ST *Distance* would make use of the ellipsoidal model and can be considered accurate enough for many applications. The query would return 933677.99m, which seems reasonable.

## 4\. View the results

Sometimes PostGIS is called *GIS without GIS*. A visual representation of spatial data is critical to understanding any geospatial problem. Without seeing it on a map, you won’t be able to fully understand the situation. However, spatial databases aren’t designed to visualize spatial data. You can, however, find a way around this. Some GIS software packages can connect directly to PostGIS to show spatial tables and queries. My favourite is QGIS.

![Figure 3— QGIS - PostGIS connection settings (image by Author)](https://towardsdatascience.com/wp-content/uploads/2021/10/1I6eWEvPBRpQKyn0BSokx2w.png)

Figure 3— QGIS – PostGIS connection settings (image by Author)

Click and select *View > Panels > Browser*. It will open *Browser Panel* for you if it is not opened by default. In the *Browser Panel*, you can find *PostGIS*. Right-click on that and choose *New Connection*. In the dialogue box, fill the options like I did (Figure 3) and test the connection. If the connection to add was successful, you could hit the *ok* button to make the connection.

A new connection with the name you have chosen (in my case: \_postgis *conn*) would appear under the *PostGIS* branch of the *Browser panel*. You can find your schemas and tables of the *postgis1* database (Figure 4). If you double-click on any of the tables, it will be shown on the map canvas and added to the layer panel. Layers can be turned on and off, exported, and used almost as you would shapefiles.

![Figure 4— Connection between PostGIS and QGIS (image by Author)](https://towardsdatascience.com/wp-content/uploads/2021/10/18qNnA0ANukIzzk4QxZth0g.png)

Figure 4— Connection between PostGIS and QGIS (image by Author)

What if we want to show the result of a query on a map? To accomplish that, choose *Database > DB Manager…* from the main menu. In the *DB Manager,* select *Database > SQL Window*.

![Figure 5— How to show the result of a query as a layer (image by Author)](https://towardsdatascience.com/wp-content/uploads/2021/10/10QIiz_4YsS_cDwCweOU8tg.png)

Figure 5— How to show the result of a query as a layer (image by Author)

According to Figure 5, we wrote a simple query to return Asian countries, and then I hit *execute*. Then I checked the *Load as a layer* checkbox, filled the necessary fields and clicked *Load.* Surprisingly, if you check the layer panel once more, you can find a new layer with the name you have chosen (here, layer name is: \_Asian *Query*) on the layer panel.

![Figure 6 - Asian countries are displayed as a result of a query (image by Author)](https://towardsdatascience.com/wp-content/uploads/2021/10/161ptk0oLHDUb-mCxVGgEMw.png)

Figure 6 – Asian countries are displayed as a result of a query (image by Author)

With the aid of simple examples, we examined the entire workflow of tackling a spatial problem using PostGIS. PostGIS can do a lot more, but the workflow is the same for many spatial challenges.