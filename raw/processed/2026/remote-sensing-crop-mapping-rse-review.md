## ReviewRemote sensing for crop mapping: A perspective on current and future crop-specific land cover data products

[https://doi.org/10.1016/j.rse.2025.114995](https://doi.org/10.1016/j.rse.2025.114995 "Persistent link using digital object identifier")

Under a Creative Commons [license](http://creativecommons.org/licenses/by-nc-nd/4.0/)

Open access

## Highlights

- •
	First review on remote sensing of crop mapping from data product perspective.
- •
	Evaluated over 60 crop-specific land cover data products and systems.
- •
	Conducted systematic literature review based on 129 papers related to CDL.
- •
	Outlined visions and progress on the development of future data products.

- [Next article in issue](https://www.sciencedirect.com/science/article/pii/S0034425725003967)

## Keywords

Crop mapping

Land use land cover

Geospatial data product

Systematic literature review

Cropland data layer

## 1\. Introduction

Crop mapping is a crucial research area within environmental remote sensing and the cornerstone for producing crop-specific land cover data (;;; ). The proliferation of crop mapping approaches and data products has been driven by several key developments. First, the volume of Earth Observation (EO) data has surged from various satellite missions, such as Landsat, Sentinel, the Moderate Resolution Imaging Spectroradiometer (MODIS), and the Visible Infrared Imaging Radiometer Suite (VIIRS). At the same time, rapid advancements in land use and land cover (LULC) mapping technologies, especially artificial intelligence (AI) and machine learning (ML), have significantly improved algorithms and models for crop type classification (;; ). Furthermore, cloud-based geospatial data hubs, such as Copernicus Data Space Ecosystem and NASA EarthData, along with all-in-one computing platforms like Google Earth Engine (GEE) () have greatly reduced the cost of accessing EO data and substantially accelerated implementation of LULC mapping (; ). The growing trend toward open data within the scientific community has also broadened the range of contributors (e.g., governments, universities, and private entities) and led to the democratization of geospatial data products (). These advances have greatly expanded the capacity of remote sensing for crop mapping at regional, national, and even global scales (;; ).

For remote sensing in agriculture, a crop mapping task can refer to both cropland extent mapping (i.e., distinguishing between crop and non-crop areas) and crop type mapping (i.e., identifying specific crop types). This paper mainly focuses on crop type mapping within the context of crop-specific land cover data production. The remote sensing community has extensively investigated the identification of spectral signatures and temporal patterns for crops (;; ). By leveraging this knowledge with image processing techniques, detailed crop type maps can be generated across large geographic areas by performing LULC classification on EO data. Through systematic analysis, validation, and scaling, these crop mapping results are processed into consistent, user-ready geospatial data products, which are then made available to the public for subsequent applications and research ().

Some well-known crop-specific land cover data products include the Cropland Data Layer (CDL) of the U.S. Department of Agriculture (USDA) National Agricultural Statistics Service (NASS), Annual Crop Inventory (ACI) of the Agriculture and Agri-Food Canada (AAFC), and MapBiomas' Land Cover and Use Maps for Brazil. Each product is suitable for specific use scenarios due to its unique spatiotemporal coverage, resolution, and data sources. For instance, CDL offers crop-specific land cover data for the entire Conterminous United States (CONUS). Similarly, ACI delivers annual maps for Canada's major croplands, while MapBiomas offers crop type maps for Brazil. These data have become essential resources for studies in multidisciplinary fields, such as LULC change (; ), crop yield (), environmental sustainability (), economic stability (), and the global food supply chain ().

Despite a plethora of available crop type maps, users often struggle to choose the most suitable one for their needs and are sometimes unaware the data products exist. Currently, there is a clear absence of a guiding reference that summarizes these data products or details their capabilities and practical values. Therefore, a systematic review of state-of-the-art crop mapping data and tools is urgently needed by the LULC community, agricultural sectors, policymakers, and stakeholders. This paper aims to fill that gap by providing the first comprehensive review of remote sensing in crop mapping from the geospatial data product perspective. Beyond serving as a reference for stakeholders seeking to use the existing data in their work, we also propose a series of research recommendations and outline visions for the development of new data products in the future.

This review is organized as follows: Section 2 presents an in-depth analysis of over 60 open-access operational data products, archival crop type maps, single-crop extent maps, crop pattern data, and related systems and platforms; Section 3 features a case study on CDL – one of the most widely used products within the remote sensing community – through a systematic literature review of 129 CDL-related papers through three research questions: (1) What EO data are used with CDL? (2) What scientific problems and technologies are explored using CDL? (3) What role does CDL play in remote sensing applications? Section 4 highlights the recent emerging topics in crop mapping and visions of future data products. Our conclusions and key takeaways are provided in Section 5.

## 2\. Overview of crop-specific land cover data products

Crop mapping has transitioned from experimental research into operational practice over the past few decades. Unlike experimental results in research settings, which often tolerate uncertainty, bias, and limited reproducibility, the geospatial data products are usually developed using operational workflows and validated methods to meet strict standards of consistency, accuracy, and timeliness (). While challenges like limited ground truth data, the complexity of cropping systems, and difficulties in scaling methods across regions persist, they also present great opportunities for the LULC community to refine operational methods and develop new data products at national to global scales.

The production of crop-specific land cover data employs remote sensing imagery to identify and classify the types of crops cultivated within a certain region. As illustrated in, sensors on board satellites capture crop type features by interacting with croplands on the Earth's surface through reflected solar radiation, emitted thermal radiation, or reflected signals from active sensors (e.g., SAR, LiDAR). These EO data are then transmitted to a ground station and undergo a chain of processing steps (e.g., radiometric and geometric calibration, corrections for atmospheric effects, and adjustments for terrain distortions) to produce ready-to-use digital imagery. Specifically, the images captured throughout the growing season contain the unique phenological features of different crop types, which can be used for crop mapping with tailored classification models and algorithms. In some cases, particularly for operational data products, crop type classification is performed within cropland areas of existing cropland masks. The final product is a geospatial dataset of crop type maps categorized by product types, crop-specific information, spatial coverage, and temporal aspects.

![Fig. 1](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr1.jpg)

Download: Download high-res image (1MB)

This section covers the major open-access data and systems that are publicly available on government or agency websites, as well as those published in peer-reviewed journals and open data repositories. Based on their distinctive characteristics, we categorize the crop-specific land cover data into: (1) operational data products; (2) archival data type maps; (3) single-crop extent maps; and (4) cropping pattern data. Additionally, common systems and applications in support of crop mapping data production and dissemination are highlighted.

### 2.1. Operational data products

Operational data products are datasets that are routinely generated, processed, standardized, and disseminated as part of ongoing, systematic operations. For agricultural LULC, operational crop-specific land cover products are vital for the sustained observation of the spatial distribution of detailed crop cover at regional or national scale. These data must meet strict quality and timeliness standards to serve a broad array of users and stakeholders. Given the substantial investment required for labor and long-term support, they are typically operated by government agencies and continuously refined using new data sources and mapping approaches, and extensively utilized as benchmarks or reference data in numerous remote sensing studies. summarizes the pivotal operational data products with core attributes for major national products. Note that data products that are operational but not primarily derived from EO data are not included in this study.

Table 1. Examples of operational crop-specific land cover data.

| Product | Temporal Coverage | Spatial Coverage | Resolution | Data   Source | Description |
| --- | --- | --- | --- | --- | --- |
| USDA NASS Cropland Data Layer | 1997 to present | CONUS | 10-m/30-m | Landsat, Sentinel-2,   ResourceSat-2 | Maps for over 100 land cover classes with 85 % to 95 % accuracy for major crop types (; ) |
| AAFC Annual Crop Inventory | 2009 to present | Canada | 30-m | Landsat, Sentinel-2, AWiFS, Radarsat-2 | Maps with over 70 land cover categories with approximately 85 % accuracy () |
| MapBiomas Land Cover and Land Use Map | 1985 to present | Brazil | 30-m | Landsat | LULC maps with major crops in Brazil with an average accuracy of 89 % () |
| CLMS High Resolution Layer Crop Types | 2017 to 2021 | EU | 10-m | Sentinel-1, Sentinel-2 | Pan-European level cropland layers of the 19 crop type classes () |
| In-season Cropland Data Layer (ICDL) | 2022 to present | CONUS | 30-m | Landsat, Sentinel-2 | In-season CDL-like maps updated monthly from May to July using mapping-without-ground-truth approach () |
| CADWR Statewide Crop Mapping | 2014 to present | California, USA | Vectorized | Landsat, NAIP | Statewide crop maps for major crop types in the State of California () |
| Crop Map of England (CROME) | 2016 to present | England, UK | Vectorized | Sentinel-1, Sentinel-2 | Maps for over 15 main crop types of UK and other land covers () |
| Queensland Crop Monitoring Program | 1987 to present | Queensland, Australia | 30-m | Landsat,   Sentinel-2,   MODIS | Biannual maps for major summer and winter crop types of Queensland, Australia () |

**USDA NASS Cropland Data Layer**: USDA NASS CDL is a pioneering operational crop-specific land cover data product that offers categorized geo-referenced crop type mapping for over 100 land cover classes. The current production of CDL relies on multisource satellite imagery acquired from Landsat 8/9 Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) sensors, Sentinel-2 A and 2B sensors throughout the growing season. The land cover classification of the 2024 CDL was performed on GEE, while a decision tree (DT) approach with RuleQuest See5.0 software was used from 2007 to 2023 (). Meanwhile, NASS incorporates ground reference data from Common Land Unit (CLU) data of USDA Farm Service Agency (FSA) () for training and validation, and the USGS National Land Cover Dataset (NLCD) () for mapping non-agricultural land cover. Some CDL states incorporate additional ground reference data from the US Bureau of Reclamation, NASS Citrus Data Layer (internal use only), and state government agencies. These improvements have made CDL a more reliable source of field-level crop cover in recent years, with a classification accuracy of 85 % to 95 % for major crop types across the CONUS.

**AAFC Annual Crop Inventory**: ACI is an annual 30-m crop type map dataset for Canada, produced by the Earth Observation Team of the Science and Technology Branch (STB) of AAFC. Similar to CDL, the production of ACI also utilizes optical (e.g., Landsat, AWiFS, Sentinel-2) and radar (e.g., Radarsat-2) satellite images, processed with the See5 DT algorithm (). The ground reference data for training and validation are from crop insurance companies, local governments, and regional AAFC Research and Development centers (). The first ACI dataset became available in 2009, initially as an experiment within the Prairie Provinces. Following its success, the ACI coverage expanded to other provinces starting from 2011. Since then, AAFC has operationally delivered annual crop type maps with an overall accuracy of approximately 85 % at the national scale (). The most recent 2022 ACI product has over 70 land cover categories, encompassing all major crop types in Canada.

**MapBiomas Land Cover and Land Use Map**: MapBiomas is a multi-disciplinary network that has developed a novel approach to reconstruct annual LULC information for Brazil since 1985. Produced using the Landsat data archive, the MapBiomas LULC map includes five major land cover classes (i.e., forest, non-forest natural formations, farming, non-vegetated areas, and water), with the average overall accuracy of 89 % ranging from 73 to 95 % in different biomes (). In particular, the Level 4 categories include major annual crops (e.g., soybean, sugarcane, rice) and perennial crops (e.g., coffee, citrus) in Brazil. Since 2016, the MapBiomas project has continually refined both the quality and the methodology of its LULC data. Starting with Collection 6, the classification leveraged 90 spectral and temporal metrics from Landsat surface reflectance images for each year, then classified using random forest (RF) and U-Net convolutional neural network (CNN). Collection 7 and 8 expanded to a total of 29 LULC classes with new crop types, such as cotton and oil palm ().

**CLMS High Resolution Layer Crop Types:** The Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Crop Types is a pan-European level LULC product and is part of the CLMS HRL Croplands portfolio (). It provides raster data layers for 19 crop type classes at 10-m resolution with target producer and user accuracies of 80 %, which is generated with a temporal transformer-based neural networks primarily using Sentinel-1 and Sentinel-2 data. First published in 2024, the initial HRL Croplands release covers the years 2017 to 2021. According to the CLMS roadmap, future updates will extend the temporal coverage through 2024, with spatial coverage expected to include the UK.

**Other operational products**: There are several other national and regional-scale products currently operated by universities, research institutes, and local governments or agencies. To fill the gap in early or in-season CDL-like data, the In-season Cropland Data Layer (ICDL) was developed and operationally released monthly from May to July. The ICDL was produced using a mapping-without-ground-truth approach (), which has been demonstrated scalable across the CONUS (). The California Department of Water Resources (CADWR) has developed a vector dataset for statewide crop mapping to enhance water use estimates and aid regional planning. The mapping workflow uses the USDA's National Agriculture Imagery Program (NAIP) for field delineation, Landsat imagery for crop classification, and field data collected from over 15 % of all irrigated lands in the Central Valley, among which 25 % are reserved for validation (). The provisional 2022 statewide crop mapping contains a total of 478,059 fields and 15,649,733 acres (approximately 6,333,222 ha) in California with overall accuracy of 98 % at the crop class legend level and 97 % at the subclass legend level (). Crop Map of England (CROME) is another vector dataset operated by the UK Government's Rural Payments Agency (RPA). It is an annual product created using the RF model with Sentinel-1 and Sentinel-2 images, containing approximately 32 million hexagonal cells classifying England into over 15 main crop types, grassland, and non-agricultural land covers (). Similarly, the Queensland Crop Monitoring Program, run by the Queensland Government, provides biannual maps identifying major summer and winter crop types in Queensland, Australia, since 1987. This program employs a phenology prediction approach based on time-series models of Landsat, Sentinel-2, and MODIS data ().

### 2.2. Archival crop type maps

The archival crop type maps are indispensable baseline data in bridging the spatiotemporal gaps left by operational data products. These data often result from state-of-the-art experimental research, but some of them may not receive routine updates or continued operation. Nonetheless, the methodologies and technologies used are generally rigorously documented and published through scientific papers. Consequently, they serve as valuable resources that offer supplementary reference data in parallel with operational products. showcases examples of archival crop type maps, which are grouped into single-year maps, multi-year datasets, refined datasets, and harmonized datasets.

Table 2. Examples of archival crop type map datasets.

| Product | Temporal Coverage | Spatial Coverage | Resolution | Data Sources | Description |
| --- | --- | --- | --- | --- | --- |
| ESA WorldCereal 10-m v100 | 2021 | Global | 10-m | Sentinel-1, Sentinel-2, Landsat | Global-scale seasonal map of temporary crops, maize, and spring/winter cereals () |
| China Crop Map | 2019 | China | 10-m | Sentinel-2, PlanetScope | Annual crop map of maize and soybean at OA of 92 % () |
| EU Crop Map | 2018/2022 | EU | 10-m | Sentinel-1, Sentinel-2 | Map for 19 crop types based on LUCAS with accuracy of 80 % (; ) |
| Argentina National Map of Crops | 2018/2019 | Argentina | 30-m | Landsat | Crop type map of main agricultural areas of Argentina () |
| National-scale Crop- and Land-cover Map of Germany | 2016 | Germany | 30-m | HLS | Land cover map with 81 % OA for 12 crop type classes () |
| National Cropland Mapping of Japan | 2015 | Japan | Vectorized | Sentinel-1, Landsat | Land cover map for 9 major crop types of Japan with overall accuracy of 87 % () |
| Crop Type Map of Jos Plateau, Nigeria | 2019/2020 | Jos Plateau, Nigeria | 10-m | Landsat,   Sentinel-2, SkySat | Map of maize, potato, and intercropping for key agricultural region in Nigeria at 84 % OA () |
| China Cropping Pattern (ChinaCP) | 2015 to 2021 | China | 500-m | MODIS | Maps of major cropping pattern systems in China at 89 % OA () |
| National-scale Crop Type Maps of Germany | 2017 to 2019 | Germany | 10-m | Sentinel-1, Sentinel-2, Landsat | Crop type mapping for 24 agricultural land cover classes with OA of 78 %–80 % () |
| GFSAD Annual Crop-type Maps | 2001 to 2014 | CONUS | 250-m | MODIS | Crop type map for 8 major crop classes with accuracy of over 75 % () |
| Crop Maps for Continental United States | 2000 to 2018 | CONUS | 231-m | MODIS | Crop type map for 8 major crop classes that reaching accuracy of 90 % by August () |
| Land Use and Cover Maps for Mato Grosso State | 2001 to 2017 | Mato Grosso State, Brazil | 250-m | MODIS | Classification of 9 LULC classes with OA of 96 % and incorporating with sugarcane, water, and urban masks () |
| Corn-Soy Data Layer (CSDL) | 1999 to 2018 | Midwestern US | 30-m | Landsat | Reconstruction of CDL-like historical corn and soybean mapping () |
| Refined Cropland Data Layer (R-CDL) | 2017 to 2023 | CONUS | 30-m | CDL | Refined CDL maps by removing noisy pixels using DT () |
| GEDI-S2 Tall/Short Crop Maps | 2019 to 2021 | Global | 10-m | GEDI, Sentinel-2 | Annual maps based on binary classification of tall and short crops () |
| EuroCrops | 2018 to 2021 | EU | Vectorized | N/A | Harmonized dataset of geo-referenced polygons for agricultural croplands from 16 EU countries () |
| GEOGLAM Best Available Crop Specific Masks | 2000 to 2021 | Global | 0.05 degrees | 24 national and regional datasets | Harmonized crop mask for maize, soybean, rice, winter wheat, and spring wheat covering 66 countries () |

**Single-year maps:** The single-year map offers a snapshot of crop cover for a specific year. The European Space Agency (ESA) WorldCereal system, for example, has generated a set of global, seasonal, and reproducible temporary crop extent, crop type, and irrigation maps, including the ESA WorldCereal 10-m v100 product which contains global-scale annual and seasonal land cover maps of temporary crops, maize, and spring/winter cereals for 2021 (). Another example is the EU Crop Map, which is a 10-m land cover map of 19 crop types across the European Union (EU) based on Sentinel-1, Sentinel-2, and Land Use/Cover Area frame Survey (LUCAS) data (; ). Other featured single-year national and regional maps include the 2019 maize-soybean map of China (), the 2016 land cover map of Germany (), the 2015 national cropland mapping of Japan (), the 2018/2019 National Map of Crops Argentina (), and the 2019/2020 crop type map of Jos Plateau, Nigeria ().

**Multi-year datasets**: Multi-year datasets aggregate consecutive single-year maps to capture temporal trends within a defined period. The Global Food Security-Support Analysis Data (GFSAD) is a NASA-funded project aiming to provide high-resolution global cropland data and their water use (). GFSAD offers a set of MODIS-derived 250-m maps for 8 major crops of U.S. (e.g., corn-soybean, wheat-barley, potato, alfalfa, cotton, rice, other crops, fallow) from 2001 to 2014 (). The China Cropping Pattern (ChinaCP) comprises crop mapping datasets from 2015 to 2021 of China, utilizing MODIS with phenology-based algorithms (). developed a dataset covering major crop classes in CONUS from 2000 to 2018 using multivariate spatiotemporal clustering with MODIS land surface phenology. released 2001–2017 LULC map datasets for Mato Grosso State, Brazil. innovatively combined Sentinel-2 with NASA's Global Ecosystem Dynamics Investigation (GEDI) data to map tall and short crops from 2019 to 2021.

**Refined datasets**: Refined datasets enhance the quality and reliability of existing data products through additional processing, such as correcting errors, resolving inconsistencies, and integrating supplementary data sources. There are a few datasets using ML and post-processing to refine operational data products like CDL. used harmonic regression and RF over the Landsat archive to create a set of Corn-Soy Data Layer (CSDL) to fill the data gaps of CDL prior to 2008. developed a Refined CDL (R-CDL) dataset by removing the noisy pixels over croplands in the original CDL using a DT strategy informed by historical spatiotemporal crop information.

**Harmonized datasets**: Harmonized datasets integrate multiple regional and national LULC datasets into a standardized format, ensuring consistency and comparability across different geographical and administrative regions. The Group on Earth Observations Global Agriculture Monitoring (GEOGLAM) Best Available Crop Specific Masks (BACS) is a global crop mask for maize, soybean, rice, winter wheat, and spring wheat that harmonized 24 national and regional datasets between 2000 and 2021 (). EuroCrops is another vectorized geo-referenced polygon dataset for EU agricultural croplands harmonized using existing datasets from government agencies across 16 EU countries (), which has combined with Sentinel-2 time series for few-shot crop type classification ().

### 2.3. Single-crop extent maps

Single-crop extent maps are specialized datasets that offer detailed insights into the spatial distribution of individual crop types. Much like the archival crop type maps, most single-crop extent map datasets emerge from experimental research. lists examples of single-crop extent map datasets. Our survey indicates that these datasets primarily focus on dominant crop types (i.e., corn, soybeans, wheat, rice) due to their importance for commodity markets and food security worldwide. Certain datasets also concentrate on minor yet high-value crops.

Table 3. Examples of single-crop extent map datasets.

| Product | Temporal Coverage | Spatial Coverage | Resolution | Data Sources | Description |
| --- | --- | --- | --- | --- | --- |
| China Maize Maps | 2017 to 2021 | China | 10-m | Sentinel-2 | Annual maize cropland maps with OA at 0.83–0.95 () |
| China Crop Dataset–Maize | 2001 to 2020 | China | 30-m | Landsat, MODIS | Annual distribution map of maize with accuracy at 80 % () |
| One-season Maize Cropland Maps | 2013 to 2021 | Northern China | 30-m | Landsat | Maize map in one-season cropland of China at R <sup>2</sup> of 0.85 with statistical yearbooks () |
| High-Resolution Crop and Maize Area Mapping for Malawi/ Ethiopia | 2016 to 2019 | Malawi and Ethiopia | 10-m | Sentinel-1, Sentinel-2 | Seasonal maize cultivation maps in smallholder farming systems of Sub-Saharan Africa countries with accuracy of 75 % () |
| Soybean Expansion in South America | 2001 to 2023 | South America | 30-m | Landsat, MODIS | Annual soybean maps with accuracy of 94 %–96 % and a set of derived data products () |
| ChinaSoyArea10m | 2017 to 2021 | China | 10-m | Sentinel-2 | Annual maps of soybean planting areas in 14 provinces of China with OA of 77 %–88 % () |
| Winter Wheat Mapping Datasets and Dynamics | 2001 to 2020 | China | 30-m | Landsat | Annual winter wheat mapping datasets of China with OA of 91.6 % () |
| Winter Wheat Distribution Maps | 2016 to 2018 | China | 30-m | Landsat, Sentinel-2 | Early-season winter wheat map of 11 provinces in China with OA of 89 % by April () |
| ChinaWheat10 | 2020 to 2022 | China | 10-m | Sentinel-1, Sentinel-2 | In-season mapping of winter wheat with OA of 95 % () |
| Paddy Rice Maps | 2017 | Bangladesh and Northeast India | 10-m | Sentinel-1 | Paddy rice maps in cloud-prone regions with accuracy over 90 % () |
| NESEA-Rice10 | 2017 to 2019 | Asia | 10-m | MODIS, Sentinel-1 | Annual paddy rice maps for Southeast and Northeast Asia () |
| Single-season Rice in China | 2017 to 2022 | China | 10/20-m | Sentinel-1, Sentinel-2 | Maps of single-season rice covering 21 provinces in mainland China () |
| Annual Paddy Rice Map | 2019 | Southeast Asia | 20-m | Sentinel-1 | Annual paddy rice map with accuracy of 92 % () |
| RapeseedMap10 | 2017 to 2019 | North America, South America, and Europe | 10-m | Sentinel-1, Sentinel-2 | Annual rapeseed map of 33 countries with F1 score at 0.84–0.91 () |
| XJ\_COTTON10 | 2018 to 2021 | Xinjiang, China | 10-m | Sentinel-1, Sentinel-2 | Annual cotton maps with OA of 90 %–95 % () |
| CARM30 | 2000 to 2022 | China | 30-m | Landsat | Annual maps with average F1 score of 0.869 and 0.971 for winter and spring rapeseed () |
| Global Winter-Triticeae Crops | 2017 to 2022 | Global | 30-m | Landsat | Maps of winter-triticeae crops (e.g., winter wheat, winter barley, winter rye, and triticale) with OA of 87 % () |
| Global Sugarcane Maps | 2019 to 2022 | Global | 10-m | GEDI,   Sentinel-2 | Sugarcane map for top 13 producing countries with accuracy over 80 % () |
| Global Oil Palm Dataset | 1990 to 2021 | Global | 10/30-m | Sentinel-1,   Landsat | Oil palm extent layer and planting year layer with producer's and user's accuracy of 91 % () |
| Global Coconut Palm Layer | 2020 | Global | 20-m | Sentinel-1, Sentinel-2 | Closed-canopy coconut palm map with OA of 99 % () |
| Cocoa Plantation Map | 2017–2020 | Côte d'Ivoire and Ghana | 10-m | Sentinel-2, GEDI | Probability and binary cocoa map with OA of 88.7 % () |
| Rubber and Rubber-related Deforestation Maps | 2021 (rubber plantations), 1993–2016 (rubber-related deforestation) | Southeast Asia | 30-m | Sentinel-2, Landsat | Rubber maps with OA of 0.95 and associated deforestation maps with OA of 0.85 () |

**Corn/maize maps**: Corn, also known as maize, is the world's most produced grain, with the U.S. and China as top producers. Numerous corn-specific mapping datasets are available for China. China Maize Maps provide annual 10-m resolution maize maps from 2017 to 2021 based on a hybrid workflow of DT and RF classifiers for improved accuracy and feature representation (). The China Crop Dataset-Maize (CCD-Maize) gives a 20-year (2001−2020) maize distribution across 22 Chinese provinces by a phenology-based Time-Weighted Dynamic Time Warping (TWDTW) approach (). Addressing the challenges of small-scale farms, created maize cropland maps over one-season planting areas of China from 2013 to 2021 using a Long Short-Term Memory (LSTM) model, and identified seasonal maize cultivation from 2016 to 2019 in smallholder farming systems of Sub-Saharan Africa countries.

**Soybean maps**: As the essential protein and oil source for nutrition and industrial products, soybean is the most economically important bean in the world. South America is the leading production region of soybeans with Brazil as the top producer. developed a dataset of soybean expansion in South America from 2001 to 2023 to reflect the region's soybean frequency, forest loss, and interannual intensity. Besides South America, the U.S. and China are also major soybean production regions. The ChinaSoyArea10m dataset took a phenological- and pixel-based mapping method to detail soybean planting areas in China from 2017 to 2021 ().

**Wheat maps**: Wheat ranks as the second most-produced cereal grain after maize, and China is the world's largest producer. Focusing on 11 provinces in China, employed the TWDTW method to create early-season winter wheat distribution maps from 2016 to 2018. Building on this work, refined the winter wheat mapping dynamics and extended the temporal coverage from 2001 to 2020. The ChinaWheat10 dataset comprises 10-m wheat maps for primary wheat-producing provinces in China from 2020 to 2022, which were created using automated training sample generation and model transfer ().

**Rice maps**: Rice is another cereal grain that serves as a staple food for more than half of the global population, especially in Asia. NESEA-Rice10 dataset integrated Sentinel-1 and MODIS data using a rule-based method to map paddy rice in Southeast and Northeast Asia from 2017 to 2019 and effectively reduced mixed-pixel issues (). utilized the TWDTW method for mapping single-season rice in China by aligning time series data with standard rice growth patterns. focused on the complexities of rice distribution in mainland Southeast Asia and employed a combination of spatiotemporal statistical features and a U-Net semantic segmentation model to produce a paddy rice area map. developed 2017 paddy rice maps in Bangladesh and Northeast India by using RF to delineate paddy rice planting over cloud-prone areas.

**Maps for other crops**: Numerous land cover datasets for less common but economically significant crops have also attracted increasing attention in recent years. The RapeseedMap10 database integrates spectral and polarization features with Sentinel-1 and Sentinel-2 data for annual mapping of 2017–2019 rapeseed across 33 countries (). The CARM30 dataset combines multi-source data including satellite imagery, environmental variables, and terrain data to create annual rapeseed maps in China from 2000 to 2022 (). XJ\_COTTON10 employs a two-step mapping strategy using time-series satellite data and RF classifier for 10-m cotton mapping across Xinjiang (). introduced a global 30-m winter-triticale crop mapping dataset of 2017–2022 across 65 countries based on the sample-free Winter-Triticale Crops Index (WTCI). developed the first 10-m global sugarcane map in the top 13 producing countries by utilizing GEDI and Sentinel-2 data to identify the unique growth characteristics of sugarcane. Additionally, global and regional maps of the permanent tree crops, such as oil palm (), coconut palm (), cocoa (), and rubber (), have become available more recently.

### 2.4. Cropping pattern data

Beyond the spatial distribution of crop cover, the crop mapping time series also contains abundant cropping pattern (e.g., crop sequence, frequency, boundaries) information. Thus, assorted cropping pattern data are derived from the existing crop-specific land cover data, especially the long-term data like CDL. shows examples of cropping pattern products and datasets. By identifying trends in crop diversification and land use intensity, these data provide insights into agricultural practices and temporal dynamics of land use.

Table 4. Examples of cropping pattern map datasets.

| Product | Temporal Coverage | Spatial Coverage | Resolution | Data Source | Description |
| --- | --- | --- | --- | --- | --- |
| CDL Crop Frequency Layer | 2008 to 2024 | CONUS | 30-m | CDL | Crop planting frequency maps for corn, soybeans, wheat, and cotton () |
| Crop Sequence Boundaries | 2008 to 2024 | CONUS | 30-m | CDL, TIGER | Cropland field boundaries with crop sequence information (; ) |
| CLMS High Resolution Layer Cropping Patterns | 2017 to 2021 | EU | 10-m | Sentinel-1, Sentinel-2 | Cropping pattern layers of emergence, harvest, the length of the bare soil period, and crop rotation cycles () |
| Maps of crop sequence types | 2012 to 2018 | EU | N/A | LUCAS dataset | Harmonized map for 31,159 points of crop sequence types and land use () |
| Global Map of Planting Years | 1982 to 2020 | Global | 30-m | Landsat | Maps of planting years of tree crops () |
| Planting Date Maps | 2000 to 2020 | Midwestern U.S. | 30-m | CDL, Landsat | Crop planting date maps for 12 states in U.S. Corn Belt () |

**Crop frequency maps**: The crop frequency map identifies planting frequency for specific crop types. For example, NASS released the crop frequency layer for four major crop types (i.e., corn, cotton, soybeans, and wheat) derived from the historical CDL of 2008 to the current year. This layer reveals planting probabilities that can enhance survey estimates and support various applications from environmental assessment to bioenergy research ().

**Crop sequence maps**: The crop sequence map charts the crop rotation patterns of each cropland field within an agricultural region over time. The Crop Sequence Boundaries (CSB) is another USDA NASS product in cooperation with the Economic Research Service (ERS), which produces estimates of field boundaries, crop acreage, and crop rotations across the CONUS (). The CSB maps deliver the 8-year cropping sequence by aggregating historical CDL into field-level polygons of homogeneous crop rotations (; ). generated the first map of dominant crop sequences in the EU, which includes 31,159 points of crop sequence type information derived from the LUCAS dataset.

**Planting date maps**: Planting date maps track the timing of crop planting across particular regions, utilizing satellite data and advanced modeling to accurately predict planting schedules. leveraged the long-term Landsat archive to map the planting years of tree crops at global scale with the LandTrendr algorithm, which has been found effective for yield prediction and cost-benefit analyses. utilized Landsat data and extensive ground samples to produce the 30-m maps of planting day-of-year (DOY) for maize and soybeans across the U.S. Corn Belt from 2000 to 2020. Associated with the HRL Crop Types, the HRL Cropping Patterns is another CMLS Croplands product that offering key agricultural characteristics, such as emergence, harvest, the length of the bare soil period, and crop rotation cycles, across the EU at 10-m resolution from 2017.

### 2.5. Systems and applications

In addition to datasets, the LULC community has implemented a range of systems and applications that have substantially enhanced the accessibility of data products and the scalability of state-of-the-art crop mapping approaches. summarizes common data service systems, web applications, and open-source projects.

Table 5. Examples of crop mapping systems and platforms.

| Product | Link | Description |
| --- | --- | --- |
| CropScape | [https://nassgeodata.gmu.edu/CropScape/](https://nassgeodata.gmu.edu/CropScape/) | Data service system for CDL data dissemination and analysis based open geospatial standards () |
| CroplandCROS | [https://croplandcros.scinet.usda.gov/](https://croplandcros.scinet.usda.gov/) | Platform for exploring CDL data powered by ArcGIS Online |
| MapBiomas Land Cover and Use Platform | [https://plataforma.brasil.mapbiomas.org/](https://plataforma.brasil.mapbiomas.org/) | Platform for MapBiomas LULC data visualization, analysis, and statistics |
| iCrop - In-season Crop Mapping Explorer | [https://cloud.csiss.gmu.edu/icrop/](https://cloud.csiss.gmu.edu/icrop/) | Data service system for in-season crop mapping exploration based open geospatial standards () |
| CropWatch | [http://cloud.cropwatch.com.cn/](http://cloud.cropwatch.com.cn/) | Platform for global crop condition, crop type, and crop production monitoring and analysis () |
| CADWR Land Use Viewer | [https://gis.water.ca.gov/app/CADWRLandUseViewer/](https://gis.water.ca.gov/app/CADWRLandUseViewer/) | Data portal for exploring CADWR statewide crop mapping powered by ArcGIS Online |
| Crop Monitor Exploring Tool | [https://cropmonitortools.org/tools/cmet/](https://cropmonitortools.org/tools/cmet/) | Web exploring tool for crop conditions, crop calendars, and crop production data by GEOGLAM |
| WorldCereal Visualization Portal | [https://vdm.esa-worldcereal.org](https://vdm.esa-worldcereal.org/) | Web data portal for WorldCereal products exploration and statistics |
| WorldCereal Classification Module | [https://github.com/WorldCereal/worldcereal-classification](https://github.com/WorldCereal/worldcereal-classification) | Python package for generating cropland and crop type maps at a wide range of spatial scales () |
| UMD GLAD Earth Engine Apps | [https://glad.earthengine.app](https://glad.earthengine.app/) | Earth Engine App gallery for UMD GLAD LULC products |
| ACTIVE v1.6 | [https://agriwatch.projects.earthengine.app/view/active](https://agriwatch.projects.earthengine.app/view/active) | Earth Engine App for rapidly visualizing CDL and conducting crop-specific land cover change detection () |
| AgKit4EE - In-season Crop Mapping Kit | [https://czhang11.users.earthengine.app/view/agkit4ee-inseason](https://czhang11.users.earthengine.app/view/agkit4ee-inseason) | Earth Engine App of automatic in-season crop type mapping for CONUS () |
| AgKit4EE- Crop Frequency Explorer | [https://czhang11.users.earthengine.app/view/agkit4ee-crop-frequency-explorer](https://czhang11.users.earthengine.app/view/agkit4ee-crop-frequency-explorer) | Earth Engine App of crop frequency mapping for CONUS () |
| RiceMapEngine | [https://cloud.csiss.gmu.edu/servir/rice-explorer/phenology](https://czhang11.users.earthengine.app/view/agkit4ee-crop-frequency-explorer) | GEE-based web application of rice mapping for Nepal () |
| Sen2-Agri | [https://github.com/Sen2Agri/Sen2Agri-System](https://github.com/Sen2Agri/Sen2Agri-System) | Open-source system to generate crop type map from Senteinel-2 and Landsat 8 data () |
| CropHarvest | [https://github.com/nasaharvest/cropharvest](https://github.com/nasaharvest/cropharvest) | Open-source dataset of global crop labels for ML-based crop type classification () |

**Data service systems**: The data service systems are generally referring to web-based geographic information systems (GIS) with full functionality for disseminating, analyzing, and managing LULC data, often equipped with application programming interface (API) for professional users and developers. CropScape is a web-based data service system for CDL data exploration and analysis based on the open geospatial standards, such as Web Map Service (WMS), Web Coverage Service (WCS), and Web Processing Service (WPS) (). CroplandCROS is a new ArcGIS Online web application to host CDL data and comes with the ArcGIS REST Services. MapBiomas Land Cover and Use Platform offers an integrated approach to MapBiomas LULC data visualization, analysis, and statistics, enabling users to navigate through multiple data layers effectively. The iCrop - In-season Crop Mapping Explorer inherits the system architecture of the well-known CropScape for exploring in-season crop mapping data as early as July (). CropWatch, as one participant of GEOGLAM initiative, is a crop monitoring platform for global crop condition, crop type, and crop production monitoring and analysis ().

**Web applications**: The web applications are online data portals and apps intuitively designed for easy visualization and exploration of crop mapping data. CADWR Land Use Viewer is a web app for visualizing the CADWR Statewide Crop Mapping data products powered by ArcGIS Online. Crop Monitor Exploring Tool is a web data portal for current and historical crop conditions, crop calendars, and crop production data by GEOGLAM. WorldCereal Visualization Portal is an interactive data portal for exploring WorldCereal products and statistics for global cereal production. It is noteworthy that GEE has greatly simplified the implementation of LULC mapping data apps. For example, a gallery for the University of Maryland (UMD) Global Land Analysis and Discovery (GLAD) LULC products is hosted on the Earth Engine App platform. AgKit4EE is a GEE-based toolkit with a suite of LULC mapping capabilities, such as generating on-demand crop sequence and crop frequency map back to 1997 () and automatic in-season crop type classification for the CONUS (). Agricultural Cropland Tracking & Interactive Visualization Environment (ACTIVE) () is a new GEE web application developed at USDA NASS that allows rapid visualization of CDL and crop-specific land cover changes (e.g., crop rotation, urbanization, and abandoned land), while also providing NDVI-based crop phenology and temporal crop entropy to track crop change frequency and diversity at any time and location across CONUS.

**Open-source projects**: As an emerging trend, some crop mapping methods are distributed as open-source projects via publicly accessible repositories. Sen2-Agri is an open-source system designed to harness the capabilities of the Sentinel-2 mission for operational agriculture monitoring at a national scale (). The crop type maps created by the Sen2-Agri system use an RF classification approach based on in situ data collected during the relevant growing season (). As a part of the NASA Harvest consortium, CropHarvest is an open-source datasets of global agricultural land use labels () and has been integrated into the Task-Informed Meta-Learning (TIML) model for crop type classification (). The WorldCereal project also released its classification module as a Python package for generating scalable cropland and crop type maps ().

## 3\. Systematic literature review: A case study on CDL

The data products reviewed in Section 2 have been widely utilized across diverse studies and applications. This section presents a systematic literature review focused on the CDL, one of the most extensively utilized products within the LULC community, to uncover key trends in the usage and impact of crop-specific land cover data in remote sensing studies. We first examine research trends of remote sensing studies related to CDL (Section 3.1), followed by a detailed review protocol (Section 3.2). The results (Section 3.3) are structured around three research questions: the use of EO data, the scientific challenges addressed and technological approaches employed, and the role of crop type maps in remote sensing applications.

### 3.1. Research trends

As the most representative national-scale field-level crop-specific land cover data product, CDL has played a pivotal role in monitoring U.S. croplands since 1997. Its significance is reflected in continuous operation by USDA NASS (e.g., ongoing refinements in mapping algorithms, input data sources, and product specifications over time), adherence to comprehensive standardized metadata (e.g., FGDC-1998 and ISO 19115), and distribution via open-access geospatial data service systems (e.g., CropScape, CroplandCROS). Owing to these features, CDL has been widely adopted and stands as an exemplary case for developing crop mapping data products. According to the user statistics on Google Analytics as presented in, more than 330,000 users from 190 countries and regions have accessed or downloaded CDL data through CropScape between 2012 and 2023.

![Fig. 2](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr2.jpg)

Download: Download high-res image (406KB)

More importantly, the wealth of literature available that incorporates CDL in remote sensing studies makes it an ideal dataset for investigation in this literature review. displays the publication counts based on the terms “Cropland Data Layer” and “Remote Sensing” indexed by Scopus and Google Scholar from 2004 through 2023. The bar chart reveals a consistent and notable increase in the number of publications related to CDL over the past two decades. Since 2019, over 500 new CDL-related publications have been indexed by Google Scholar and 200 by Scopus within a single year. By analyzing all CDL-related publications to date, we found 60 % of them include the term “remote sensing” (with 3530 of 6102 on Google Scholar and 1615 of 2265 on Scopus). These publication statistics demonstrate the relevance and broad impact of crop-specific land cover data in the field of remote sensing.

![Fig. 3](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr3.jpg)

Download: Download high-res image (440KB)

### 3.2. Review protocol

We conducted a systematic literature review referring to the guidelines established by, which has been widely adopted by review articles in the field of remote sensing, agriculture, and environmental sciences (;;; ). The review protocol was developed with the following components: research questions, database selection, search criteria, and protocol validation.

#### 3.2.1. Research questions

This review analyzes existing literature that incorporates the use of CDL from multiple perspectives. To extract the latest advancements and key features of CDL in the context of remote sensing, we have formulated three research questions (RQs) and outlined the objective for each RQ in.

Table 6. Research questions.

| ID | Research Question | Objective Description |
| --- | --- | --- |
| RQ1 | What EO data are used with CDL? | Identify common and suitable EO data in conjunction with crop type maps in remote sensing field |
| RQ2 | What scientific problems and technologies are explored using CDL? | Understand the state of the science and main technologies in remote sensing that are applied with crop type maps |
| RQ3 | What role does CDL play in remote sensing applications? | Help researchers to recognize the significance of crop type maps and consider how to incorporate into these data their own work |

#### 3.2.2. Database selection

As shown in, approximately 1300 publication records are indexed by Scopus and 3000 publication records are indexed by Google Scholar based on the keyword “Cropland Data Layer” and “Remote Sensing”. However, this result encompasses different types of publications (e.g., journal articles, conference articles/abstracts, dissertations/theses, reports, and presentations) and some of them are not qualified in this review. For example, the search results in Google Scholar included government reports that used CDL as supporting data. A few studies had preliminary results published in conference papers or abstracts, with the full research later published in journal papers. Several publications only included the relevant keywords in their reference sections, rather than in the article's title, abstract, or keywords.

To screen the representative studies among all publications, we chose the Web of Science (WoS) Core Collection as the database and established a set of query criteria to screen the qualified publications that used CDL as the data source in the remote sensing field. To include more qualified literature, we expanded the literature database by incorporating articles from the CDL citations featured on the official USDA NASS website ().

#### 3.2.3. Search criteria

lists the search criteria to screen qualified publications within the database. To set clear boundaries for the review and ensure that only relevant studies were included, we defined three inclusion criteria (IC) to restrict the journal articles related to CDL and remote sensing, and three exclusion criteria (EC) to exclude irrelevant articles from the screened results. The logical relationship between all criteria is an “AND” operator, which means that a publication must meet all inclusion criteria and none of the exclusion criteria to be considered relevant for our study.

Table 7. Document search criteria.

| ID | Description |
| --- | --- |
| Inclusion Criteria 1 (IC1) | “Cropland Data Layer” OR “CDL” contained in any fields |
| Inclusion Criteria 2 (IC2) | Category in “Remote Sensing” or in other categories but contain “Remote Sensing” or “Earth observation” or “Landsat” or “Sentinel” or “MODIS” in any fields |
| Inclusion Criteria 3 (IC3) | Publication is a journal article |
| Exclusion Criteria 1 (EC1) | The full term of “CDL” is not related to “Cropland Data Layer” |
| Exclusion Criteria 2 (EC2) | No remote sensing data is used in the study |
| Exclusion Criteria 3 (EC3) | Publication is a review paper |

In the process of publication selection, each search criterion was designed with a specific purpose. The IC1 specifies that the keyword “Cropland Data Layer” or “CDL” must appear in any field of metadata in the WoS database, including the publication title, abstract, or keywords. In our survey, we found that many papers introduced, discussed, or cited CDL, but did not directly use the data in their experiments. Therefore, IC1 could ensure that CDL has been applied in the selected publications, rather than simply mentioning it in passing.

To narrow down the publications to those specifically related to remote sensing, IC2 states that the publication's “Category” field in the WoS database must be labeled as “remote sensing”. However, many publications related to remote sensing were published in computer science, agricultural, or multidisciplinary journals, which were not categorized as “remote sensing”. To include these publications in this review, we added a rule that requires the presence of certain terms, such as “Remote Sensing”, “Earth observation”, “Landsat”, “Sentinel”, or “MODIS” in any of the title, keywords, or abstract of the publication.

To ensure the selected publications reflected the up-to-date research trends and avoided duplicate research items, IC3 limits the document type to only peer-reviewed articles that were published in journals indexed by the WoS Core Collection. Focusing on these high-impact journal articles guarantees that our review reflects the most representative studies within the remote sensing field.

The query string of inclusion criteria in the WoS data database is: *ALL = (“Cropland Data Layer” OR “CDL”) AND (WC = “Remote Sensing” OR ALL = (“Remote Sensing” OR “Earth observation” OR “Landsat” OR “Sentinel” OR “MODIS”)) AND DT = “Article”*, where ALL represents all fields (title, abstract, keywords), WC represents WoS categories, and DT represents document type. After the initial screening process, we manually applied the three exclusion criteria to exclude publications where the full term “CDL” was not related to “Cropland Data Layer”, studies that did not use remote sensing data, and any review articles. These exclusion criteria were essential for ensuring the reliability of our selection results and for eliminating any irrelevant literature. The literature selection process from the CDL citations on the USDA NASS website adheres to the same inclusion and exclusion criteria. The eligible documents were combined with the screening results of WoS database, and any duplicate records were removed.

### 3.3. Results

The result of the literature screening process is illustrated in. Applying the inclusion criteria, we screened 162 and 43 articles from the WoS database and the USDA NASS CDL website, respectively. We then excluded 48 and 8 non-qualified articles from the two sources. After removing the 20 duplicated records, we identified 129 qualified articles for use in this systematic literature review. The full literature list and surveyed features per selected publication are summarized in.

![Fig. 4](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr4.jpg)

Download: Download high-res image (158KB)

summarizes the publication distribution of 129 qualified articles across over 40 scientific journals. It should be noted that these screening results only encompass representative articles related to the CDL in remote sensing science. As documents are searched based on keywords within titles and abstracts, studies that used CDL as data source but did not mention it in these fields remain unidentified and are not reflected in the screening results. All records in the database were published before December 31st, 2023.

Table 8. Publication distribution of the qualified CDL-related remote sensing studies by journals.

| Journal | Record Count |
| --- | --- |
| Remote Sensing of Environment | 27 |
| Remote Sensing | 26 |
| International Journal of Applied Earth Observation and Geoinformation | 9 |
| ISPRS Journal of Photogrammetry and Remote Sensing | 9 |
| Photogrammetric Engineering and Remote Sensing | 4 |
| Agronomy Journal | 3 |
| Computers and Electronics in Agriculture | 3 |
| Remote Sensing Letters | 3 |
| Agricultural Systems | 2 |
| Agricultural Water Management | 2 |
| Canadian Journal of Remote Sensing | 2 |
| Earth System Science Data | 2 |
| European Journal of Remote Sensing | 2 |
| IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing | 2 |
| International Journal of Remote Sensing | 2 |
| Science of Remote Sensing | 2 |
| Sensors | 2 |
| Others (only one paper) | 27 |
| Total | 129 |

#### 3.3.1. RQ1: What EO data are used with CDL?

reveals that a diverse range of EO data has been employed in remote sensing science with CDL over the years. This trend indicates that MODIS and Landsat are the two most used data associated with CDL, appearing in 64 and 50 publications, respectively. The NLCD serves as another notable remote-sensing-based land cover data product, which is compared and investigated with CDL in 12 research papers. Following the launch of the Sentinel missions, the Sentinel-2, Sentinel-1, and Harmonized Landsat Sentinel-2 (HLS) data have gained momentum in CDL-related research in recent years. In addition, 16 papers have utilized other remote sensing data.

![Fig. 5](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr5.jpg)

Download: Download high-res image (332KB)

**MODIS**: Since operation began in 1999, MODIS has been delivering long-term, continuous daily observations of Earth's surface through 36 spectral bands at spatial resolutions of 250-m, 500-m, and 1 km. The Terra and Aqua MODIS Surface Reflectance products (MOD09/MYD09) have been extensively studied alongside the CDL. Due to its high temporal resolution, the MODIS Surface Reflectance time series serves as a valuable data source for rapid crop mapping and crop progress monitoring (;; ). A variety of data products have been derived from MODIS. For instance, the MODIS Vegetation Index Products (MOD13 and MYD13) offer Level-3 global mapping of the Normalized Difference Vegetation Index (NDVI) and the Enhanced Vegetation Index (EVI) at spatial resolutions of 250-m, 500-m, and 1 km, available in sub-monthly and monthly intervals. The CDL has been utilized in conjunction with MODIS NDVI in many remote sensing applications (;;;; ). It has also been employed as reference data to examine MODIS products. For example, used CDL in combination with a set of commonly utilized MODIS products, such as NDVI and EVI (MOD13Q1), Fraction of Photosynthetically Active Radiation (FPAR) and Leaf Area Index (LAI) (MOD15A2 and MYD15A2), and Gross Primary Production (GPP) (MOD17A2 and MYD17A2), to explore their correlation with crop yields. incorporated CDL as reference data to compare MODIS LAI (MOD15) and Land Cover Type (MOD12).

**Landsat**: As the primary data source for producing CDL, Landsat shares the same 30-m spatial resolution and has been used with CDL for field-level studies (;;; ). CDL has been investigated with Landsat 5 (launched in 1984 and end of service in 2013), Landsat 7 (launched in 1999), Landsat 8 (launched in 2013), and Landsat 9 (launched in 2021). Among the selected literature, Landsat 5/8 are by far the most frequently used Landsat satellites, and it is anticipated that Landsat 9 will be increasingly used in the upcoming research. Due to the malfunction of the Thematic Mapper (TM) scan line corrector, a gap-filling process is required before using Landsat 7 data with CDL (). Landsat data are often combined with MODIS and other sources to generate higher temporal resolution fused data in CDL-related research (;;; ). The widespread use of GEE in recent years has greatly simplified access to Landsat data and significantly accelerated field-level analysis at the regional and national scale ().

**NLCD:** NLCD serves as another input data source for CDL, particularly for non-crop classes (). Both the NLCD and CDL programs are incorporated by the Multi-Resolution Land Characteristics (MRLC) Consortium (). Sharing the same spatial coverage and resolution, NLCD and CDL have been jointly used to assess cultivated cropland and estimate agricultural area (;;; ). conducted a systematic analysis of LULC change using CDL and NLCD data. A few studies have integrated these two datasets to quantify forest area (; ).

**Sentinel-2**: Developed by ESA, Sentinel-2 offers 10-m resolution multispectral data. The Sentinel-2A and -2B satellites, launched in June 2015 and 2017 respectively, have reduced the moderate-to-high-resolution observation interval of Earth's surface to 5 days. As a system similar to Landsat but with superior spatiotemporal resolution, Sentinel-2 has been employed alongside CDL for more accurate and timely crop type mapping and agricultural monitoring (;; ).

**Sentinel-1**: Sentinel-1 provides synthetic aperture radar (SAR) data suitable for applications like land and sea monitoring as well as natural disasters mapping. It is frequently used as an auxiliary data source with Landsat and Sentinel-2 data to support data fusion for crop monitoring (;; ). Moreover, CDL has been integrated with Sentinel-1 data for rice mapping () and crop lodging assessment ().

**HLS**: Integrating imagery from the Landsat and Sentinel-2 satellite, the Harmonized Landsat and Sentinel-2 (HLS) dataset further enhanced temporal coverage and continuity in the existing EO datasets (; ). The HLS has been coupled with CDL to streamline the time-series-based remote sensing applications, such as crop emergence and phenological progress monitoring (;; ).

**Other data sources**: In addition to the above data, more EO data sources are used alongside CDL to address specific tasks in environmental remote sensing. explored the 3-m Planet Fusion data and CDL for tillage practice mapping. used Soil Moisture Active Passive (SMAP) and CDL as input data source for flood progress monitoring in cropland. investigated the land surface phenology and seasonality by coupling the Advanced Microwave Scanning Radiometer (AMSR) passive microwave data with CDL. used Earth Observing (EO-1) Hyperion hyperspectral images and CDL to classify five major crop types in the world and their growth stages. CDL has been used with Global Ozone Monitoring Experiment-2 (GOME-2) and Orbiting Carbon Observatory 2 (OCO-2) data to investigate solar-induced chlorophyll fluorescence for agricultural monitoring and crop yield prediction (; ).

**Data fusion:** Data fusion has been an evolving trend to enhance the quality and reliability of EO data. CDL was incorporated in data fusion approaches that blend Landsat and MODIS data for crop progress mapping (;,; ). fused a suite of MODIS products to map plant functional types and compared with CDL. Sentinel-1 data have also been fused with Landsat and Sentinel-2 data to enrich land surface features (; ), and growing applications of optical and SAR data fusion have enhanced crop identification of smallholder fields and specialty crop types (; ). The combinations of EO data sources for all surveyed publications are summarized in the “EO Data” column of.

#### 3.3.2. RQ2: What scientific problems and technologies are explored using CDL?

shows the trends of scientific problems and technologies explored in the selected literature. Four major research topics are identified, where crop mapping and classification has the most publications, followed by LULC change analysis, crop yield estimation and forecasting, and crop phenology detection and monitoring. Notably, these scientific problems are increasingly being addressed with ML technologies, particularly deep learning (DL), in recent years.

![Fig. 6](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr6.jpg)

Download: Download high-res image (385KB)

**Crop mapping and classification**: As an essential component of environmental remote sensing, crop mapping and classification provide critical information on the spatial distribution of crop types. CDL is often employed as benchmark data for validating crop classification results in early-year applications (;; ). With the proliferation of moderate-to-high-resolution satellite data, early- and in-season crop classification have become prominent topics in recent years. CDL has emerged as a crucial tool for developing and enhancing early- and in-season crop type classification algorithms and workflows (;;;; ). A range of methods have been employed to provide essential information for monitoring crop cover at regional or CONUS scale (;;;; ). Numerous studies have used CDL as a reference to develop methods for mapping rice (), corn and soybeans (; ), rapeseed (), cotton (), potatoes (), winter wheat (), and other crop types. Some papers have also explored the development of generalizable and transferable crop type classification models based on CDL (; ).

**Crop yield estimation and forecasting**: The combination of CDL and EO data offers a powerful approach for modeling crop growth dynamics and enhancing the accuracy of crop yield prediction. used CDL as reference data to systematically assess the correlation between MODIS data and the yield of all major crop types in the United States. Corn and soybeans are the two most frequently studied crops in yield estimation and forecasting. and developed a model to estimate soybean cultivated areas at national scale. and studied the county-level corn yield prediction. and assessed the corn and soybean yield forecasting using a data fusion approach. and combined CDL with a regression model on MODIS time series to enhance crop area estimation. CDL is also applied to MODIS and GlobCover land cover product for global cropland area estimation ().

**Crop phenology detection and monitoring**: Crop phenology reflects crop growth stages and health throughout the growing season. Many studies have enhanced our understanding of crop phenology by integrating CDL with time-series EO data to track and analyze changes in vegetation indices, such as NDVI and EVI. explored real-time monitoring of crop phenology using daily VIIRS and MODIS time series. applied a within-season crop emergence algorithm to derive green-up maps during the growing season. developed a hybrid phenology matching model to retrieve crop phenological stages using MODIS time series., focused on field-scale corn and soybean phenology detection. Furthermore, time series analysis has also been used in phenology-based satellite image classification () and spatially constrained phenological mixture analysis ().

**Land use land cover change**: With long-term, national-scale, field-level crop information, CDL effectively captures LULC change of new planted areas on formerly non-agricultural lands (e.g., abandoned farmland, land restorations, agri-tourism, prior industrial uses), as well as crop abandonment due to development, reforestation, and idle/fallow. These comprehensive spatial and temporal characteristics make it highly suitable for examining the shifts in land use patterns and the impact of these changes on the environment, especially changes in cropland area (), crop rotation patterns (; ), and the conservation tillage practices (). conducted a comprehensive investigation into CDL's capabilities for LULC change analysis. utilized CDL and MODIS time series data to analyze bioenergy agricultural land use changes and biomass quantities. used CDL and Landsat data to track land cover change for the western edge of the U.S. Corn Belt back to 1984. quantified marginal land for the CONUS by analyzing time series of CDL and history of satellite-observed land use change.

**Machine learning**: ML models and algorithms like DT, RF, Support Vector Machine (SVM), and Artificial Neural Network (ANN) have been extensively used with CDL for a wide range of tasks. Among the literature reviewed, RF is the most prevalent ML model, which has been extensively applied in cropland extent mapping () and crop type classification (;; ). SVM is another widely used ML algorithm and well-suited for remote sensing tasks due to its ability to handle high-dimensional data and its robustness against overfitting (; ). used DT with CDL and MODIS MOD09Q1 to map 2001–2014 crop cover for the CONUS. Some studies have focused on comparing different ML models in crop mapping and crop yield estimation (;;;; ). Meanwhile, transfer learning has emerged as a strategy in environmental remote sensing to address domain shift and improve transferability of ML models (), among which was the first to test the transferability for crop type classification model using CDL as training samples.

**Deep learning**: As a subset of ML, DL employs deep neural networks (DNNs) to recognize patterns in EO data and has gained significant attention for its high accuracy and efficiency in classification tasks. CDL has been used as input to DNNs and demonstrated promising results in crop mapping and crop type classification (;; ). More complex DL architectures, such as CNNs and Recurrent Neural Networks (RNNs), are also implemented incorporating with CDL. CNNs have proven to be effective for LULC classification tasks by learning hierarchical feature representations from remote sensing data (;; ). RNNs (e.g., LSTM) capture temporal dependencies and have been used to model cropping patterns in CDL time series (;;; ). U-Net is an optimized architecture for semantic segmentation tasks featuring an encoder-decoder structure with skip connections to learn and retain high-resolution features, which has provided detailed segmentation results of LULC and crop cover (;; ).

#### 3.3.3. RQ3: What role does CDL play in remote sensing applications?

As shown in, the trends of CDL's role in the literature review suggests CDL plays a multifaceted role in remote sensing applications. Specifically, CDL is commonly utilized as a crop mask during the EO data preparation, as training samples for modeling and classification, and as benchmark data for result validation.

![Fig. 7](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr7.jpg)

Download: Download high-res image (317KB)

**Crop mask**: One of CDL's primary functions is serving as a crop mask to isolate pixels of interest for the specific crop types in the remote sensing imagery. This technique is frequently employed to extract pure crop pixels in analysis of crop types and land cover patterns (;;;; ) or to exclude certain crops and unqualified pixels (). CDL data also have been used to delineate and stratify regions, such as U.S. soybean growing areas (), which helps in understanding field size patterns for more effective agricultural resource management.

**Training samples**: Beyond a crop type map, CDL is widely utilized as an authoritative geospatial benchmark to support field-level crop spectral signature training. The ML models trained with high-confidence pixels in CDL and associated products (e.g., CSB, Confidence Layer) can be applied to extend land cover classification while adjusting for factors such as hemisphere seasonality and evolving farming trends, which is invaluable for global crop monitoring. As discussed in RQ2, ML and DL are the main technologies in remote sensing studies, which rely on high-quality training data. Due to the extensive crop-specific land cover information, CDL has been extensively used to label training samples in EO data. This enables the further supervised-learning-based training process for semantic segmentation models (), ML models (), DL models (; ), and transfer learning models (; ). Instead of directly using CDL as training samples, some works further optimized the training sample selection process by modeling crop rotation patterns in the historical CDL (). and used DNNs to automatically recognize training samples from CDL time series to label Landsat and Sentinel-2 data for early and in-season crop mapping.

**Benchmark data**: CDL is often adopted as benchmark data or reference data to validate new crop mapping methodologies and algorithms. The traditional ground-truthing process is usually labor-intensive, particularly when surveying extensive geographic areas. By comparing results against the CDL, researchers can efficiently assess model performance, detect areas for improvement, and refine their strategies to achieve optimal outcomes. However, despite its widespread use, it should be noted that CDL only represents a high-quality classification map rather than ground truth. Several studies have examined the uncertainty and potential biases associated with using CDL as benchmark data for result validation. For example, found the average accuracy for all crop classes has improved from 87 % in 2008 to 92 % in 2016. showed 2019–2020 CDL had 89 % accuracy evaluated with independent ground truth data within the central US Corn Belt.

**Other uses**: CDL and its derivative data products have been applied in addressing broader applications and scientific problems. developed a stratification method for agricultural area sampling frame construction based on CDL. used CDL to assist in the creation of Bidirectional Reflectance Distribution Function (BRDF) look-up maps. Harmonic analysis techniques, such as linear and non-linear harmonic models, have been employed with CDL to model periodic patterns in time series data (; ). evaluated different time-series smoothing algorithms. developed a signal-to-noise ratio method to identify spatially homogeneous vegetation cover. CDL has also been utilized in GIS education () and as compared dataset for particular purposes (;;;; ).

## 4\. Visions for future data products

As science and technology in remote sensing advances, the demand for enhanced crop-specific land cover data products becomes increasingly evident. This section explores vision and progress in improving spatiotemporal coverage and resolution of the current data products (Section 4.1), achieving reliable global mapping through robust training datasets and cropland extent data (Section 4.2 and 4.3), incorporating more crop-specific information (Section 4.4 and 4.5), and the development of operational in-season crop mapping systems (Section 4.6).

### 4.1. Progress on enhanced coverage and resolution of current product

Enhanced spatial coverage and resolution significantly benefit crop mapping, area estimation, and field size quantification by enabling more accurate identification of land cover features. Advancement in geospatial cloud computing platforms (e.g., GEE) and increasing availability of higher spatiotemporal resolution open EO data (e.g., Sentinel-1, Sentinel-2, HLS) have improved the efficiency and accuracy for producing regional and national crop type map data with resolution of 10-m or even higher (; ). Such detailed field-level crop cover information will not only facilitate a more precise distinction between different types of vegetation and crops, but also provide opportunities for improved agricultural monitoring, better resource management, and informed decision-making to support sustainable agriculture and food security.

As highlighted in the Section 3, the 30-m CDL has traditionally been essential for scientific problem solving with various EO data. However, the increasing availability of higher-resolution EO data from both open-access and commercial satellites requires more detailed crop mapping products. To meet this evolving need, the USDA NASS has been enhancing data accuracy and usability by implementing a 10-m resolution CDL. These improvements are vital, particularly given the increasing vulnerability of agriculture to natural disasters and extreme weather events. By utilizing the RF algorithm, enhanced stratified random sampling approaches, and localized image processing, the 10-m CDL provides a more accurate representation of diverse crop types for CONUS, particularly in regions with unique or specialty crops. This methodology reduces labor and workload while improving classification accuracy and spatial clarity for small-area and specialty crops compared to 30-m CDL. shows the improvement achieved with the new 10-m CDL compared to the current 30-m CDL on croplands with complex landscapes.

![Fig. 8](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr8.jpg)

Download: Download high-res image (3MB)

Currently, the CDL is available only for the CONUS. However, efforts are underway to extend coverage to other regions, such as Hawaii and U.S. territories like Puerto Rico and the U.S. Virgin Islands. Enhanced CDLs for these areas include the 2022 Beta version and the official 2024 release of the 10-m resolution CDL for CONUS (), and the inaugural Hawaii Cropland Data Layer (HCDL) 2023 and 2024 (). These products leverage gap-filled 10-day image composites from Sentinel and Landsat sensors, processed through GEE. In developing the HCDL, assorted ML and DL algorithms were evaluated, including RF, U-Net, ResNet50, VGG19, and DeepLabV3. The RF algorithm achieved the best results for mapping major and specialty crops in Hawaii. illustrates the 10-m resolution HCDL 2023 V1.0 Beta, which utilizes a RF algorithm with 100 trees for mapping crops, including coffee, pineapple, macadamia nuts, commercial forest, citrus, papaya, and tropical fruits. The official release of HCDL 2023 and 2024 is anticipated in summer 2025. Future efforts will focus on creating a 10-m resolution annual CDL for CONUS and potentially extending to Puerto Rico and the U.S. Virgin Islands.

![Fig. 9](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr9.jpg)

Download: Download high-res image (1MB)

### 4.2. Developing training dataset in data-sparse regions

Lack of training data is a major barrier for developing crop type maps like CDL in regions outside of the United States or other countries that have instituted operational mapping programs (e.g., programs in ). Researchers aim to overcome this barrier in two main ways: (1) developing more globally representative training datasets, and (2) developing algorithms that learn more efficiently from small amounts of training data.

**Globally representative training datasets:** Globally representative reference data is essential for training modern data-hungry DL models and has been identified as a key priority in advancing AI applications in remote sensing (). Collecting crop type data for training ML classifiers for crop mapping is challenging because collecting high-quality data typically requires ground-truthing (). Ground-truthing involves physically visiting agricultural fields and recording the type of crop growing in the field. This process is prohibitively expensive and logistically challenging for many organizations and regions.

Currently available public reference samples are largely regional in scope (; ). Recent work has proposed novel methods of collecting ground-truth crop labels that reduce the cost of data collection. proposed a method called Street2Sat that uses computer vision (CV) techniques to transform roadside images of fields collected with car- and motorcycle helmet-mounted cameras into geo-referenced crop type labels of those fields. used CV techniques to extract crop type and phenology information from street-level images of fields taken with car-mounted cameras in the Netherlands. and used DL models to automatically create crop type labels from Google Street View images in California and Thailand, respectively.

Other work leveraged crowd-sourced data from online and mobile platforms to collect ground-truth crop data. used crop type data crowd-sourced from the Plantix mobile app (used to help farmers diagnose crop disease) for crop mapping in India. demonstrated the use of the mobile app Picture Pile to engage citizen scientists to annotate crop type labels in crowdsourced street-level images from Mapillary, which could later be converted to geo-referenced crop type labels for training crop mapping models. The CropObserve app facilitated the process on crop-specific ground truthing (e.g., crop types, phenological stage, visible damage, management practices) anywhere in the world ().

In parallel with data collection efforts, increasing attention is being paid to making crop type reference data more Findable, Accessible, Interoperable, and Reusable (FAIR). Major research initiatives (e.g., CropHarvest, WorldCereal, and EuroCrops) are actively working on harmonizing, standardizing, and openly publishing training datasets to enhance the FAIRness of crop reference data within the remote sensing and agricultural monitoring communities.

**Algorithms that learn more efficiently from small amounts of training data:** To reduce the need for large labeled datasets to train effective crop mapping models, researchers have proposed methods for learning from a small amount of training data for a given location. Many of these methods involve learning from labeled data in locations other than the target region to supplement training. The WorldCereal project trained a CatBoost classifier with expert-designed features extracted from multiple satellite datasets using a reference database of globally distributed crop type labels (). Other work has leveraged transfer learning, in which models are first “pre-trained” on a large labeled dataset for one task (e.g., crop mapping in region A) and then further trained (“fine-tuned”) on a smaller dataset for the target task (e.g., crop mapping in region B). Meta-learning algorithms are also used to learn efficiently from a small number of crop type examples in a new target region by learning from many globally-distributed crop type classification tasks in the CropHarvest dataset (, ).

Researchers have developed methods for learning generic features that are useful in diverse tasks (e.g., crop mapping, land cover mapping, tree species classification) from a large amount of unlabeled satellite EO data in a process called self-supervised learning. Similar to transfer learning discussed previously, after a model is pre-trained using self-supervised learning, it can be fine-tuned for a specific crop mapping task. For example, proposed a self-supervised model called Presto (which stands for **P** re-trained **re** mote **s** ensing **t** ransf **o** rmer) that learns from unlabeled EO data from multiple satellite platforms and derived products. They showed that fine-tuning Presto on the Kenya maize classification task and Brazil coffee classification task in CropHarvest achieved state-of-the-art performance. Both tasks required learning from small training data sizes of 1345 in Kenya and 203 in Brazil. In Phase II of the ESA WorldCereal project (2024-2026) (), Presto was adopted for feature extraction for crop type mapping in place of the expert-designed features used to train a CatBoost classifier in. With Presto's robust algorithm for improving spatiotemporal transferability, this integration is key to WorldCereal's aim of establishing a generic and customizable global crop mapping system.

In recent years, foundation models have emerged to address the scarcity of labeled training data in remote sensing applications (; ). For example, Google recently introduced AlphaEarth Foundations (AEF) for global mapping from sparse label data (). As a geospatial foundation model, AEF integrates multi-source, multi-modal EO and geoinformation data into a time-continuous embedding space, and the resulting global dataset of analysis-ready embedding field layers could enable a wide range of mapping tasks. Such foundation models and analysis-ready data offer a promising solution for efficient production of cropland and crop type maps at a global scale.

### 4.3. Improving consistency of cropland extent mask for global crop mapping

From the perspective of global crop mapping, a reliable and consistent cropland extent map serves as the fundamental land cover category in the crop-specific land cover data production, which are crucial for the subsequent crop type classification process especially over the data-sparse regions. Various cropland extent mask data derived from EO data have been widely developed and validated over the past years. However, selecting the most appropriate cropland extent mask and conducting local validation of these data tailored to the specific requirements of the study remains challenging due to inconsistency and variability in their reported accuracies and cropland definitions.

To improve consistency and transparency of cropland extent, developed an agreement map based on six global cropland products, revealing significant disagreements in Western Europe, South America, and Africa. These findings are consistent with cropland accuracy assessments conducted by both data providers and independent researchers, which report global cropland map accuracies ranging from 65 % to 90 % (;;;; ). Efforts also have been made to generate more consistent cropland maps by correcting the patterns in the disagreement hotpot regions ().

Another major challenge in comparing cropland extent products lies in the variation of cropland definitions, making it essential to identify and understand these definitional differences when analyzing discrepancies among products (). gives the definition of cropland for FAOSTAT cropland area statistics. The cropland of FROM-GLC includes greenhouses, whereas WorldCover omits them. WorldCereal aligns its cropland mapping with the “temporal crops” definition sourced from, a definition also used by WorldCover. Similarly, GFSAD30's cropland extent definition closely resembles that of FAOSTAT's “cropland”, whereas GLAD and Dynamic World exclude woody crops, close to the FAOSTAT delineation of “arable land”. ESRI land cover also has a similar definition to “arable land”, but the paddy rice field is excluded. Conversely, GLC-FCS30 encompasses herbaceous and woody crops but overlooks pasture and fallow land. Globeland30 included herbaceous crops, planting pasture, woody crops and greenhouse but excluding fallow land. In contrast, FROM-GLC includes permanent shrub crops while excluding tree crops.

Table 9. FAO land use categories for cropland.

| Land Use Category | Definition |
| --- | --- |
| Cropland | Land used for cultivation of crops. The total of areas under Arable land and Permanent crops. |
| Arable land | Land used for cultivation of crops in rotation with fallow, meadows and pastures within cycles of up to 5 years. The total of areas under Temporary crops, temporary meadows and pastures, and temporary fallow. Arable land does not include land that is potentially cultivable but is not cultivated. |
| Temporary crops | Land used for crops with a less than 1-year growing cycle, which must be newly sown or planted for further production after the harvest. Some crops remaining in the field for more than 1 year may also be considered as temporary crops (e.g., asparagus, strawberries, pineapples, bananas, and sugar cane). Multiple-cropped areas are counted only once. |
| Temporary fallow | Land that is not seeded for one or more growing seasons. The maximum idle period is usually less than 5 years. This land may be in the form sown for the exclusive production of green manure. Land remaining fallow for too long may acquire characteristics requiring it to be reclassified as, for instance, permanent meadows and pastures if used for grazing or haying. |
| Temporary meadows and pastures | Land temporarily cultivated with herbaceous forage crops for mowing or pasture, as part of crop rotation periods of less than 5 years. |
| Permanent crops | Land cultivated with long-term crops which do not have to be replanted for several years (e.g., cocoa and coffee), land under trees and shrubs producing flowers (e.g., roses and jasmine), and nurseries (except those for forest trees, which should be classified under “forestry”). Permanent meadows and pastures are excluded from permanent crops. |

### 4.4. Incorporating within-season crop emergence

Crop emergence indicates the status of crops in the early stages of growth. In most areas, crops have a specific growth calendar which is different from natural vegetation. The within-season crop emergence map contains information on temporal domain that could be useful for differentiating between crop and non-crop areas and potentially identifying different crop types with spectral information. Together with early- or in-season crop type maps, this information can unlock a range of new applications, such as irrigation schedule optimization, pest management, crop condition assessment, yield estimation, and biomass accumulation estimation (;, ).

Traditionally, crop emergence dates are recorded and reported by farmers on a large scale. In the United States, the USDA NASS reports state-level crop emergence data in its Crop Progress and Condition report. With the enrichment of available EO data from remote sensing satellites, such as those operated by NASA or commercial providers like Planets Labs, various crop emergence data products are derived using algorithms to detect changes in vegetation cover, which provides broad coverage and can be used to monitor large agricultural areas at field and sub-field level (;;;; ). The Terra and Aqua combined MODIS Land Cover Dynamics (MCD12Q2) data product provides global land surface phenology metrics at yearly intervals from 2001 to 2021 (; ). The vegetation phenology metrics at 500-m spatial resolution are derived from time series of the 2-band Enhanced Vegetation Index (EVI2) () calculated from MODIS Nadir BRDF-Adjusted Reflectance (NBAR) (). The VIIRS global land surface phenology inherited the MODIS MCD12Q2 curvature phenology algorithm with phenology metrics at 500 m spatial resolution since 2013 ().

USDA ARS is currently developing the operational crop emergence mapping data product. proposed the within-season emergence (WISE) algorithm for detecting green-up dates from remote sensing time series. The green-up dates are related to, but generally lag behind, crop emergence date. Previous remote-sensing based algorithms were capable of detecting green-up dates in 2–4 weeks after emergence when green leaves had developed, and the change of VI can be confirmed (; ). The WISE approach only requires observations during the early growth stages to detect crop emergence within 1–2 weeks after it occurs. It can map the crop emergence date using the limited satellite observations available during the early growth stages, with a mean difference of three days and a mean absolute difference of one week ().

WISE has been extended to five Corn Belt states (i.e., Iowa, Illinois, Indiana, Minnesota, and Nebraska) for routine mapping of crop emergence using HLS (30 m, 3–4 day revisit) data (). As illustrated in, benefiting from the frequent revisits of HLS, WISE detected the majority of fields across CONUS and provided detailed spatial variability within each field. Recent high temporal and spatial resolution satellite datasets (e.g., HLS, PlanetScope) are making it feasible for mapping within-season crop emergence over the CONUS () and have great potential for integration with in-season crop mapping data products and operational crop monitoring systems (; ).

![Fig. 10](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr10.jpg)

Download: Download high-res image (897KB)

### 4.5. Advancing national-scale crop-specific field boundary mapping

Crop-specific field boundary mapping presents crop type information with precise field boundaries in vector format, which offers great potential to enhance the quality and use of existing data products. While a number of open-access vectorized crop mapping data products exist (e.g., CADWR crop mapping), most are limited to regional scales. The CLU dataset provides national-scale vector-based crop field polygons. Although with accurate cropland boundaries, CLU is not publicly accessible, and it includes only fields that farmers self-report to the FSA. Additionally, CLUs represent administrative boundaries, which may encompass multiple crops within a single polygon (). The CSB dataset effectively addresses this gap by providing not only vectorized fields across the CONUS but also additional information, such as field boundaries, crop acreage, and crop rotations.

The CSB datasets are algorithmically delineated field polygons that enhance applications requiring large-scale crop mapping with vector-based data. The CSB algorithm is a repeatable automated process for building crop-field polygons with accurate representation of crop areas. A growing historical CDL archive and advancements in the availability of cloud computing make it possible to produce the CONUS CSB products demonstrated by. An eight-year window was published for public use, but any window between the years 2008–2023 can be used to comprise a CSB. CSB based acreages have been assessed against NASS Quick Stats estimates for corn and soybeans. The CSBs tend to be accurate though slightly on the positive side with an error of 2–5 % for corn and an error of 5–7 % for soybeans in the years 2015 through 2022 ().

The first CSB release was in July 2023 and has been revised based on public feedback. One notable change is smoothing CSBs for a more realistic look. The function used was “simplify polygon”, which applies the “retain critical bends option” based on the algorithm defined by to simplify the resulting polygons from the previous refinement steps while preserving critical bends at a 60-m tolerance. Based on user feedback requesting more realistic boundaries, this results in a smoother CSB product with less prominent stair stepping lines, an artifact of the CDL gridded data. highlights the improvement between the first version and current CSB version rev23 overlaying an area on Maryland's Eastern Shore.

![Fig. 11](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr11.jpg)

Download: Download high-res image (587KB)

Apart from the CSBs themselves, future work will involve research into applications. Similar to the CDL applications discussed in Section 3.3.2, CSB has already been integrated with ML models for pre-season crop type classification and mapping, where the predicted results were shown to be competitive with CDL based approaches for a select group of states and crop types with respect to administrative ground truth data (). Other planned enhancements include assessing prediction quality across all 48 continental US states and adding more crop types, and testing the effects of tuning parameters, such as selection of ML model and number of temporal windows used for training. Finally, broader pre- and in-season applications of CSB, such as area survey imputation and regional disaster risk assessment, will be explored.

### 4.6. Toward operational in-season crop mapping

The literature review also indicates that CDL has been widely used in the development of in-season crop mapping approaches at field level in recent years (;;;; ). However, enabling the operational in-season monitoring of field-level crop-specific land cover is still challenging due to the lack of ground truth at early growing season and difficulties in scaling ML models, particularly at regional or national scale.

To tackle these issues, developed an efficient and effective mapping-without-ground-truth workflow, which has been successfully applied in the production of the first CDL-like in-season crop-specific land cover data (i.e., ICDL) for the CONUS. As depicted in, the main advantage of this method is the use of trusted pixels, the high-confidence pixels that are predicted from CDL time series using regular crop rotation patterns (e.g., monocropping, alternate cropping), to replace ground truth and label training samples in satellite (i.e., Landsat, Sentinel-2) images for rapid crop type classification.

![Fig. 12](https://ars.els-cdn.com/content/image/1-s2.0-S0034425725003992-gr12.jpg)

Download: Download high-res image (4MB)

The production of ICDL is already in operation. The provisional dataset can be previewed and accessed through the iCrop system as described in Section 2.5 (). The current year's data is released as early as June and updated monthly through August on iCrop. In 2023, the crop cover map for May was released in early June, and the map for July was released in early August. As the growing season progresses and more satellite imagery becomes available, the accuracy of the data will keep increasing. By August, the provisional data product is expected to reach 80 %–90 % agreement with CDL.

The data processing workflow is still being fine-tuned and improved with post-processing steps to be applied in the final product. For example, CV-based image segmentation systems, such as Segment Anything Model (SAM), have shown promising results for improving accuracy and quality of the crop mapping results (; ). These refinements will undergo systematic evaluation to ensure they meet operational standards for in-season crop monitoring. Meanwhile, advanced Transformer-based architectures can directly process raw irregular time series data without requiring compositing (), which has been tested effective for CONUS-scale in-season crop type mapping with HLS data (). Planning is underway to incorporate these advancements into future operational in-season products.

## 5\. Conclusion

This comprehensive review offers valuable insights into remote sensing for crop mapping from the perspective of geospatial data products. Our survey indicates that the open EO data, notably from the moderate-to-high resolution data sources (e.g., Landsat and Sentinel-2), have enabled the production of assorted field-level crop type maps at national or regional scales with spatial resolutions as fine as 10-m to 30-m. These data products can be divided into operational data products, archival datasets, single-crop extent map datasets, and cropping pattern datasets. Many of these products are also associated with open systems and platforms.

Using CDL as an example, we conducted a synthesis analysis of 129 representative research articles in remote sensing studies utilizing crop type maps in a variety of ways. Our analysis reveals that CDL has been frequently used in conjunction with MODIS, Landsat, NLCD, Sentinel-2, and Sentinel-1 data. The top scientific challenges addressed in the remote sensing field using CDL include crop mapping and classification, crop yield estimation and forecasting, crop phenology detection and monitoring, and LULC change analysis, while state-of-the-art ML and DL technologies are commonly applied with CDL. Furthermore, CDL serves multiple roles in remote sensing applications, often being utilized as a crop mask during data preprocessing, as training samples for modeling and classification, and as benchmark data for result validation.

We also reviewed progress in critical areas for the development of future data products. Looking ahead, improving spatiotemporal coverage, as well as finer resolution, will further enhance the accuracy and usability of existing products, as demonstrated in the progress of 10-m CDL with the coverage of Hawaii and efforts to reconstruct historical crop cover. Achieving reliable global mapping will require robust training samples and standardizing methodologies, as highlighted by work on the development of training datasets in data-sparse regions and global cropland extent standardization. The integration of more abundant crop-specific information (e.g., within-season crop emergence, vectorized crop mapping algorithms) into the future data products will provide deeper insights to stakeholders across the agricultural, policy, and LULC sectors. Significant progress has also been made in developing an operational system for in-season crop monitoring across the CONUS, which enables timely field-level crop-specific LULC data and supports more responsive agricultural decision-making.

Finally, this review highlighted challenges in advancing operational crop mapping. For instance, while many crop type maps are published, their underlying training data and methodologies often remain inaccessible. Many existing crop type maps are the “one-shot” result of research projects rather than sustained operational systems, which limits their long-term value and reproducibility, especially for non-expert users who need actionable information. Concurrently, the development of closed-access national crop mapping systems can lead to duplicated efforts and wasted resources. These challenges underscore the urgent need for agricultural monitoring initiatives (e.g., GEOGLAM, EuroCrops, WorldCereal) and open data projects (e.g., CropHarvest) to enable FAIRness of crop type reference data and establish harmonized training datasets. These foundational data efforts, alongside open-access systems (e.g., Sen2-Agri, iCrop), are crucial for transitioning to more transparent and reproducible crop mapping approaches globally.

## CRediT authorship contribution statement

**Chen Zhang:** Writing – original draft, Project administration, Methodology, Conceptualization. **Hannah Kerner:** Writing – original draft. **Sherrie Wang:** Writing – original draft. **Pengyu Hao:** Writing – original draft. **Zhe Li:** Writing – original draft. **Kevin A. Hunt:** Writing – original draft. **Jonathon Abernethy:** Writing – original draft. **Haoteng Zhao:** Writing – original draft. **Feng Gao:** Writing – original draft. **Liping Di:** Writing – review & editing, Supervision, Funding acquisition. **Claire Guo:** Writing – review & editing, Validation, Investigation. **Ziao Liu:** Writing – review & editing, Investigation. **Zhengwei Yang:** Writing – review & editing, Resources. **Rick Mueller:** Writing – review & editing, Resources. **Claire Boryan:** Writing – review & editing, Resources. **Qi Chen:** Writing – review & editing, Resources. **Peter C. Beeson:** Writing – review & editing, Resources. **Hankui K. Zhang:** Writing – review & editing. **Yu Shen:** Writing – review & editing.

## Disclaimer

The findings and conclusions in this publication are those of the author(s) and should not be construed to represent any official USDA or U.S. Government determination or policy.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgment

This research is supported in parts by grants from the National Science Foundation (Grant, ), USDA NIFA (Grant, ), and USDA NASS (Grant ). The authors would also like to thank four anonymous reviewers for their valuable comments and suggestions.

## Appendix A. Selected publications in the systematic literature review

Table A1. Full list of selected publications and research features in the systematic literature review (in descending order by year).

| Publication | EO Data | Scientific Problem | Technology | Role of CDL |
| --- | --- | --- | --- | --- |
|  | Landsat, Sentinel-1, Sentinel-2 | Alfalfa mapping | ML (RF) | Result validation |
|  | Sentinel-1, Sentinel-2 | Satellite image classification | ML, ensemble classification | Training samples, result validation |
|  | MODIS | County-level soybean yield forecasting | ML (XGBoost) and DL (1D-CNN) | Reference data to mask soybean pixels |
|  | Sentinel-1 | Evaluating NISAR crop mapping data | Comparative analysis | Compared dataset in the study |
|  | Planet Fusion | Tillage practice mapping | DL | Mask crop types, result validation |
|  | MODIS | Crop yield prediction | Transfer learning | Reference data to mask corn and soybean pixels |
|  | MODIS | Corn yield prediction | DL | Reference data to mask corn pixels |
|  | HLS, ABI | Near-real-time crop progress monitoring | Data fusion | Reference data to extract corn and soybean pixels |
|  | NLCD, LCMAP | LULC products assessment | Comparative analysis | Compared dataset in the study |
|  | MODIS | Early-season crop mapping | ML (RF) | Result validation |
|  | NLCD | Analyzing consistency of forestland estimates | Overlaying and comparing data using GIS approach | Reference data |
|  | Landsat | Rice mapping | DL (U-Net) | Training samples for semantic segmentation model |
|  | Sentinel-2 | Crop mapping for corn, soybeans, rice | DL and ensemble learning | Training samples |
|  | Sentinel-2 | In-season corn-soybean mapping | DL (CNN, LSTM) | Training samples |
|  | Landsat, Sentinel-2 | Early- and in-season crop type mapping | DL (CNN), transfer learning | Generating the current-year training samples |
|  | HLS, VIIRS | Corn and soybean phenology detection | Time series analysis | Reference data mask corn and soybean pixels |
|  | Sentinel-2 | Developing 10-m resolution crop type mapping | ML (RF) | Training samples, result validation |
|  | MODIS | Improving sub-pixel mapping for high-resolution crop mapping | DL (CNN) | Result validation |
|  | Sentinel-1 | Rice mapping with limited ground truth data | DL (U-net) | Training samples for transfer learning model |
|  | Landsat | Corn dynamics mapping limited training samples | Adaptive strategies for collecting representative training samples | Training sample |
|  | MODIS | Cotton mapping using limited training samples | ML (RF, AdaBoost), DL (LSTM) | Source of auxiliary data |
|  | Landsat, MODIS | Albedo estimation using smoothed anisotropy features | BRDF Spatiotemporal Smoothing, data fusion | Land cover type evaluation |
|  | Sentinel-2 | In-season crop type mapping | ML (RF) | Generating the current-year training sample |
|  | MODIS | Crop phenology detection | Hybrid phenology matching model | Reference data to mask corn and soybean pixels |
|  | HLS | Mapping within-season crop emergence | Within-season emergence (WISE) algorithm | Reference data to generate statistics of green-up dates for corn and soybean pixels |
|  | Landsat | Improving crop mapping generalization | DL (U-Net) | Training samples |
|  | Sentinel-1, Sentinel-2 | Rapeseed mapping | Pixel- and phenology-based algorithm, data fusion | Validation for U.S. rapeseed mapping |
|  | NLCD, LIDAR | Improving aboveground forest biomass estimation | Statistical analysis | Source of forest location and typology information |
|  | MODIS | Marginal land availability assessment | Framework for quantifying economically marginal land | Identifying cropland in transition |
|  | MODIS | Producing high-resolution, real-time gross primary productivity product | ML | Derive the fraction cover of C4 crop |
|  | MODIS | Crop yield estimation | Linear modeling | Reference data to develop crop-specific masks |
|  | Landsat, Sentinel-2 | Pre- and in-season crop mapping | ML (RF) | Crop rotation modeling |
|  | Landsat, Sentinel-1 | Mapping prevent planting acres | Threshold-based change detection | Extracting fallow pixels |
|  | Landsat, NLCD | Phenology pattern-based training sample selection for land cover mapping | Automatic phenology learning | Building land cover patterns |
|  | MODIS | Corn yield prediction | DL (unsupervised adaptive domain adversarial neural network) | Reference data to mask corn pixels |
|  | MODIS | Estimating crop-specific damage after flooding event | Disaster Vegetation Damage Index | Result validation |
|  | Landsat, MODIS | Mapping irrigated corn | ML (ANN, RF, SVM) | Training samples, result validation |
|  | MODIS | Early-season crop classification | ML (RF) | Training samples, result validation |
|  | MODIS | Reconstructing daily NDVI for crops | Crop reference curve | Reference data to identify pure pixels |
|  | MODIS | Winter wheat grain production estimation | Vegetation photosynthesis model | Result validation |
|  | MODIS | Forecasting maize and soybean production | Vegetation photosynthesis model | Result validation |
|  | Landsat | Corn-soybean crop mapping | DL (LSTM), ML (RF) | Training samples, result validation |
|  | Landsat | Crop mapping | DL (CNN) | Training samples, result validation |
|  | Landsat, Sentinel-2 | In-season corn-soybean mapping | DL (DNN) | Generating training sample, result validation |
|  | Sentinel-1 | Crop lodging Assessment | Hidden Markov random field | Result validation |
|  | Sentinel-2 | Potato mapping | ML (SVM, maximum likelihood) | Training samples, result validation |
|  | Landsat | Identifying temporal and spatial behavior of the irrigation water use | Energy balance models and water balance models | Result validation |
|  | HLS | Transfer learning for crop type classification | ML (RF) | Training samples, result validation |
|  | MODIS, OCO-2 | Solar-induced chlorophyll fluorescence (SIF) extraction | ML (ANN) | Derive fractional area coverage of corn/soybean |
|  | MODIS | In-season crop mapping | Scalable cluster-then-label model based on Multivariate Spatio-Temporal Clustering (MSTC) | Training samples, result validation |
|  | Landsat | Mapping historical crop type | ML (RF) | Training samples, result validation |
|  | Landsat, MODIS | Mapping LULC changes | ML (RF) | Training samples, result validation |
|  | GOME-2, MODIS, OCO-2 | Crop yield prediction | ML (RF, SVM, ANN, LASSO, RIDGE) | Result validation |
|  | Landsat | Analyzing the effects of land use and land cover variation on hydrology and water quality | Soil and Water Assessment Tool (SWAT) | Aggregate the remote sensing variables to county level for corn and soybean |
|  | Landsat | Crop time series modeling | Linear and non-linear harmonic models | Identifying major crop types in the CONUS |
|  | MODIS | Quantifying albedo impacts of changing agricultural practices | Space-borne analysis of collocated MODIS-derived BRDF and CDL | Reference data to provide daily albedo of homogeneous agricultural fields |
|  | Landsat | Crop type classification | DL (DNN) | Training samples, result validation |
|  | Landsat | Mapping historical crop-soybean | Generalizable crop classification model | Training samples, result validation |
|  | Landsat | Corn-soybean mapping | DL (LSTM) | Training samples, result validation |
|  | AMSR | Characterizing land surface phenologies and seasonalities | Mann-Kendall trend test, paired two-sample *t* -test | Reference data to provide fine spatial resolution land cover data |
|  | Landsat | Soybean mapping | Reflectance-based North American Model | Training samples, result validation |
|  | Landsat | Mapping historical crop cover | Rule-based classification | Training samples, result validation |
|  | SMAP | Flood progress monitoring | Fusing SMAP, soil properties, floodplain data | Reference data to extract inundated croplands |
|  | Landsat | In-season crop mapping | ML (RF) | Training samples, result validation |
|  | Landsat | Crop type classification | DL (LSTM) | Training samples, result validation |
|  | Landsat | Crop mapping without field labels | ML (RF, and unsupervised Gaussian mixture models) | Training samples, result validation |
|  | MODIS | Winter wheat mapping | DL (DNN) | Result validation |
|  | EO-1 | Classifying crop type and differentiating growth stages | ML (PCA, LDA, SVM) | Training samples, result validation |
|  | Landsat | Identifying land cover change | Phenology-based satellite image classification | Result validation |
|  | MODIS, NLCD | Crop acreage estimation | Pixel counting, linear regression, Bayesian method | Reference data for crop acreage estimation |
|  | Landsat | In-season corn-soybean mapping | DL (deep neural network) | Training samples, result validation |
|  | Landsat, MODIS, Sentinel-2 | Crop yield estimation | Data fusion | Result validation |
|  | MODIS, VIIRS | Real-time monitoring of crop phenology | Logistic model | Reference data to mask corn and soybeans pixels |
|  | Landsat | Cropland extent classification | ML (RF and RHSeg) | Result validation |
|  | MODIS | Improving regional-scale crop yield forecasting | Statistical seasonal forecasting framework | Reference data to mask out the corn fields |
|  | MODIS | Understanding and comparing irrigated land datasets | Comparative analysis | Compared dataset in the study |
|  | HLS, Sentinel-1 | In-season crop mapping | ML (RF) | Training samples, result validation |
|  | Landsat | Land cover classification | Nonlinear dimensionality reduction and modified graph segmentation | Training samples, result validation |
|  | MODIS | Analyzing the effect of EVI time series density on crop classification | ML (RF, SVM, ANN, maximum likelihood, minimum distance) | Result validation |
|  | Landsat, MODIS | Mapping of crop progress and phenology | Spatial and Temporal Adaptive Reflectance Fusion Model (STARFM) | Result validation |
|  | MODIS | Crop type classification | ML (DT) | Training samples, result validation |
|  | Landsat, MODIS | Soybean area estimation | Regression tree-based models | Training samples |
|  | NLCD | Comparing   agriculture   accuracy in land   cover data | Comparative   analysis | Compared dataset   in the study |
|  | MODIS, NLCD | Measuring land use land cover change | Post-classification measurement and correction | Compared dataset in the study |
|  | MODIS | Crop mapping | ML (DT) | Training samples, result validation |
|  | MODIS | Estimating flood impact on corn yield | Regression model | Masking pure corn pixels for analysis |
|  | MODIS | Early-season winter crop mapping | Gaussian Mixture Model (GMM) | Reference data to derive a cropland mask, result validation |
|  | Landsat | Soybean mapping and area estimation | Stratified, two-stage cluster sampling with active learning | Reference data to delineate and stratify U.S. soybean growing regions |
|  | Landsat | Mapping energy crops | ML (DT) | Result validation |
|  | NLCD | Assessing NLCD cultivated cropland class accuracy | Multi Index Integrated Change Analysis (MIICA) | Result validation |
|  | MODIS | Crop mapping | ML (RF) | Training samples, result validation |
|  | MODIS | Correlating MODIS products with crop yields | Comparative analysis | Reference data to mask crop areas |
|  | MODIS, NLCD | Time-series smoothing for land-cover classification | Comparison of five smoothing algorithms | Result validation |
|  | MODIS | Mapping annual corn/soybean changes | ML (ANN) | Training samples, result validation |
|  | Landsat, MODIS | Early-season corn-soybean classification | Bayesian discriminant analysis | Reference data to construct agricultural units, result validation |
|  | Landsat | Quantifying crop field sizes | Refined automated field extraction methodology | Reference data to provide crop type information for discerning field size pattern |
|  | MODIS | In-season corn-soybean mapping | ML (RF, fuzzy classification) | Result validation |
|  | MODIS | Identifying homogeneous vegetation cover | Temporal signal-to-noise ratio (SNR) | Result validation |
|  | MODIS | Early-season crop mapping | ML (RF, Jeffries-Matusita distance) | Training samples, result validation |
|  | Landsat, SPOT | Monitoring cover crop adoption | Satellite spectral indices analysis and integration | Reference data to evaluate extent of green wintertime vegetation |
|  | Landsat, MODIS | Object-based crop type classification | ML (DT) | Training samples, result validation |
|  | MODIS | Evaluating global land cover maps | Comparative analysis | Reference data to adjust MODISLC and GlobCover estimates |
|  | Landsat, MODIS, NAIP | Improving accuracy in remote sensing classification | Data fusion | Reference data to enhance land use classification |
|  | MODIS | Analyzing the sensitivity of crop classification | ML (artificial immune network) | Training samples, result validation |
|  | Landsat | Handling missing data in multi-temporal imagery | ML (RF) | Training samples, result validation |
|  | MODIS | Crop mapping for bioenergy land use | Spatially constrained phenological mixture analysis | Result validation |
|  | AWiFS, DMC, Landsat, MODIS | Correcting angular effects for crop monitoring | Data fusion | Reference data to build BRDF look-up map |
|  | Landsat | Improving accessibility and usability of CDL in GIS education | Geoprocessing of data mashup, statistics analysis, change analysis | Reference data to benefit GIS education |
|  | MODIS | Forecasting corn and soybean yields | Regression tree-based models | Reference data to mask crop pixels |
|  | MODIS | Quantifying cropland net primary production variability | Comparing inventory, satellite-based, and process-based models | Reference data to mask crop cover pixels |
|  | Landsat | Characterizing cropping sequences and identifying land use changes | String-matching algorithm | Reference data to mask crops at field-level |
|  | MODIS | Comparing MODIS data collections for agricultural applications | Scattering by Arbitrarily Inclined Leaves (SAIL) model | Result validation |
|  | MODIS | Monitoring bioenergy-driven agricultural land use changes | ML (SVM) | Training data |
|  | NLCD, C-CAP, GAP, LANDFIRE | Comparing national land cover data products | Comparative analysis | Compared dataset in the study |
|  | Landsat, MODIS | Crop type classification | Rule-based automated cropland classification algorithm (ACCA) | Result validation |
|  | Landsat | Crop field extraction | Object-based segmentation (variational region-based geometric active contour) | Result validation |
|  | MODIS | Estimating spatially resolved cropland net primary production | Agricultural Inventory-based Light Use Efficiency (AgI-LUE) framework | Reference data to mask crop cover |
|  | NLCD | Mapping annually tilled areas | Comparative analysis | Compared dataset in the study |
|  | MODIS | Corn progress stage detection | Dimensionality-reduction-based differential box-counting algorithm | Reference data to remove non-corn pixels |
|  | Landsat | Mapping tillage practices for conservation monitoring | Object-based segmentation | Reference data to produce field-level tillage maps |
|  | Landsat | Developing GIS to disseminate CDL data | GIS, zonal statistics, change detection | Main data source for the system |
|  | MODIS | Crop type classification | ML (regression tree classification model) | Training samples, result validation |
|  | MODIS | Quantifying agricultural fire patterns | Global ordinary least squares (OLS) and local geographically weighted regression (GWR) analyses | Reference data to examine fire distribution by land cover/land use type |
|  | MODIS | Mapping perennial energy crops | ML (DT) | Result validation |
|  | Landsat, NLCD, RESOURCESAT-1, AWiFS | Parcel-based classification of agricultural crops | ML (DT) | Compared dataset in the study |
|  | Landsat | Crop type classification | ML (RF) | Result validation |
|  | MODIS | Mapping cropland and major crop types | Ecoregion-stratified two-step processing approach | Result validation |
|  | MODIS | Improve geospatial resolution of inventory-based carbon accounting | Data fusion, multisource evidential reasoning algorithm | Reference data to mask crop cover |
|  | MODIS | Plant functional type mapping | Regression tree, parsimonious model | Result validation |

## Data availability

No data was used for the research described in the article.

## References

- ### Contribution of Sentinel-1 radar backscatter/coherence and Sentinel-2 optical data to digital mapping of soil organic carbon in the Iberian Peninsula
	2026, Soil and Tillage Research
- ### Harvesting AlphaEarth: Benchmarking the geospatial foundation model for agricultural downstream tasks
	2026, International Journal of Applied Earth Observation and Geoinformation
- ### From time-series generation and model selection to transfer learning: A review and comparative analysis of pixel-wise approaches for large-scale crop mapping
	2026, Computers and Electronics in Agriculture
- ### A novel spectral and phenological composite index for the early automatic mapping of potatoes from Sentinel-2 multi-temporal images
	2026, Computers and Electronics in Agriculture
- ### Spatial aggregation trends of cultivated land quality and landscape patterns: A remote sensing analysis
	2026, Applied Soil Ecology
- ### Applications of Remote Sensing in Agricultural Soil and Crop Mapping
	2025, Agriculture Switzerland