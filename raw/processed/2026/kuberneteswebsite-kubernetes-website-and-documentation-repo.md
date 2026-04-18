## The Kubernetes documentation

This repository contains the assets required to build the [Kubernetes website and documentation](https://kubernetes.io/). We're glad that you want to contribute!

## Using this repository

You can run the website locally using [Hugo (Extended version)](https://gohugo.io/), or you can run it in a container runtime. We strongly recommend using the container runtime, as it gives deployment consistency with the live website.

## Prerequisites

To use this repository, you need the following installed locally:

- [npm](https://www.npmjs.com/)
- [Go](https://go.dev/)
- [Hugo (Extended version)](https://gohugo.io/)
- A container runtime, like [Docker](https://www.docker.com/).

> [!note] Note
> Make sure to install the Hugo extended version specified by the `HUGO_VERSION` environment variable in the [`netlify.toml`](https://github.com/kubernetes/website/blob/main/netlify.toml#L11) file.

Before you start, install the dependencies. Clone the repository and navigate to the directory:

```
git clone https://github.com/kubernetes/website.git
cd website
```

The Kubernetes website uses the [Docsy Hugo theme](https://github.com/google/docsy#readme), which can be installed via npm. You can also download a pre-configured development container image that includes Hugo and Docsy. Additionally, a Git submodule is used for tools that generate the reference documentation.

### Windows

```
# fetch submodule dependencies
git submodule update --init --recursive --depth 1
```

### Linux / other Unix

```
# fetch submodule dependencies
make module-init
```

## Running the website using a container

To build the site in a container, run the following:

```
# You can set $CONTAINER_ENGINE to the name of any Docker-like container tool

# Render the full website
make container-serve

# Render only a specific language segment (e.g., English)
make container-serve segments=en

# Render multiple languages (e.g., English and Korean)
make container-serve segments=en,ko
```

**💡 Tip:** Using *Hugo segments* speeds up local preview builds, by rendering only selected language(s).

If you see errors, it probably means that the Hugo container did not have enough computing resources available. To solve it, increase the amount of allowed CPU and memory usage for Docker on your machine ([macOS](https://docs.docker.com/desktop/settings/mac/) and [Windows](https://docs.docker.com/desktop/settings/windows/)).

Open up your browser to [http://localhost:1313](http://localhost:1313/) to view the website. As you make changes to the source files, Hugo updates the website and forces a browser refresh.

## Running the website locally using Hugo

To install dependencies, deploy and test the site locally, run:

- For macOS and Linux
	```
	npm ci
	# Render the full site (default)
	make serve
	# Render only a specific language segment
	make serve segments=en
	# Render multiple language segments
	make serve segments=en,ko
	```

**💡 Tip:** Hugo segments are defined in `hugo.toml` and allow faster rendering by limiting the scope to specific language(s).

- For Windows (PowerShell)
	```
	npm ci
	hugo.exe server --buildFuture --environment development
	```

This will start the local Hugo server on port 1313. Open up your browser to [http://localhost:1313](http://localhost:1313/) to view the website. As you make changes to the source files, Hugo updates the website and forces a browser refresh.

## Building the API reference pages

The API reference pages located in `content/en/docs/reference/kubernetes-api` are built from the Swagger specification, also known as OpenAPI specification, using [https://github.com/kubernetes-sigs/reference-docs/tree/master/gen-resourcesdocs](https://github.com/kubernetes-sigs/reference-docs/tree/master/gen-resourcesdocs).

To update the reference pages for a new Kubernetes release follow these steps:

1. Pull in the `api-ref-generator` submodule:
	```
	git submodule update --init --recursive --depth 1
	```
2. Update the Swagger specification:
	```
	curl 'https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json' > api-ref-assets/api/swagger.json
	```
3. In `api-ref-assets/config/`, adapt the files `toc.yaml` and `fields.yaml` to reflect the changes of the new release.
4. Next, build the pages:
	```
	make api-reference
	```
	You can test the results locally by building and serving the site from a container:
	```
	make container-serve
	```
	In a web browser, go to [http://localhost:1313/docs/reference/kubernetes-api/](http://localhost:1313/docs/reference/kubernetes-api/) to view the API reference.
5. When all changes of the new contract are reflected into the configuration files `toc.yaml` and `fields.yaml`, create a Pull Request with the newly generated API reference pages.

## Troubleshooting

If you experience any issues with running website locally, please refer to the [Troubleshooting section](https://kubernetes.io/docs/contribute/new-content/preview-locally/#troubleshooting) of the contributing documentation.

## Get involved with SIG Docs

Learn more about SIG Docs Kubernetes community and meetings on the [community page](https://github.com/kubernetes/community/tree/main/sig-docs#meetings).

You can also reach the maintainers of this project at:

- [Slack](https://kubernetes.slack.com/messages/sig-docs)
	- [Get an invite for this Slack](https://slack.k8s.io/)
- [Mailing List](https://groups.google.com/forum/#!forum/kubernetes-sig-docs)

## Contributing to the docs

You can click the **Fork** button in the upper-right area of the screen to create a copy of this repository in your GitHub account. This copy is called a *fork*. Make any changes you want in your fork, and when you are ready to send those changes to us, go to your fork and create a new pull request to let us know about it.

Once your pull request is created, a Kubernetes reviewer will take responsibility for providing clear, actionable feedback. As the owner of the pull request, **it is your responsibility to modify your pull request to address the feedback that has been provided to you by the Kubernetes reviewer.**

Also, note that you may end up having more than one Kubernetes reviewer provide you feedback or you may end up getting feedback from a Kubernetes reviewer that is different than the one initially assigned to provide you feedback.

Furthermore, in some cases, one of your reviewers might ask for a technical review from a Kubernetes tech reviewer when needed. Reviewers will do their best to provide feedback in a timely fashion but response time can vary based on circumstances.

For more information about contributing to the Kubernetes documentation, see:

- [Contribute to Kubernetes docs](https://kubernetes.io/docs/contribute/)
- [Page Content Types](https://kubernetes.io/docs/contribute/style/page-content-types/)
- [Documentation Style Guide](https://kubernetes.io/docs/contribute/style/style-guide/)
- [Localizing Kubernetes Documentation](https://kubernetes.io/docs/contribute/localization/)
- [Introduction to Kubernetes Docs](https://www.youtube.com/watch?v=pprMgmNzDcw)

### New contributor ambassadors

If you need help at any point when contributing, the [New Contributor Ambassadors](https://kubernetes.io/docs/contribute/advanced/#serve-as-a-new-contributor-ambassador) are a good point of contact. These are SIG Docs approvers whose responsibilities include mentoring new contributors and helping them through their first few pull requests. The best place to contact the New Contributors Ambassadors would be on the [Kubernetes Slack](https://slack.k8s.io/). Current New Contributors Ambassadors for SIG Docs:

| Name | Slack | GitHub |
| --- | --- | --- |
| Sreeram Venkitesh | @sreeram.venkitesh | @sreeram-venkitesh |

## Localization READMEs

| Language | Language |
| --- | --- |
| [Bengali](https://github.com/kubernetes/website/blob/main/content/bn/README.md) | [Korean](https://github.com/kubernetes/website/blob/main/content/ko/README.md) |
| [Chinese](https://github.com/kubernetes/website/blob/main/content/zh-cn/README.md) | [Polish](https://github.com/kubernetes/website/blob/main/content/pl/README.md) |
| [French](https://github.com/kubernetes/website/blob/main/content/fr/README.md) | [Portuguese](https://github.com/kubernetes/website/blob/main/content/pt-br/README.md) |
| [German](https://github.com/kubernetes/website/blob/main/content/de/README.md) | [Russian](https://github.com/kubernetes/website/blob/main/content/ru/README.md) |
| [Hindi](https://github.com/kubernetes/website/blob/main/content/hi/README.md) | [Spanish](https://github.com/kubernetes/website/blob/main/content/es/README.md) |
| [Indonesian](https://github.com/kubernetes/website/blob/main/content/id/README.md) | [Ukrainian](https://github.com/kubernetes/website/blob/main/content/uk/README.md) |
| [Italian](https://github.com/kubernetes/website/blob/main/content/it/README.md) | [Vietnamese](https://github.com/kubernetes/website/blob/main/content/vi/README.md) |
| [Japanese](https://github.com/kubernetes/website/blob/main/content/ja/README.md) |  |

## Code of conduct

Participation in the Kubernetes community is governed by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md).

## Thank you

Kubernetes thrives on community participation, and we appreciate your contributions to our website and our documentation!