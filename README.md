# "doi2bib-web" 

A simple web service that brings bibtex from DOI number. it uses [doi2bib](https://github.com/bibcure/doi2bib) on background.

## Running the server locally

* Build with `docker build . -t doi2bib-web`
* Start with `docker run -p 8080:8080 doi2bib-web`
* Open in your browser at `http://localhost:8080/?url=sampledoi