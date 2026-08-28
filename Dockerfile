# Dockerfile ----------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Container definition for production pipeline environment.

# Base R image
FROM rocker/r-ver:4.4.1

# System dependencies required by R packages
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install renv package
RUN R -e "install.packages('renv', repos='https://cloud.r-project.org/')"

# Copy renv lockfile and configuration for layer caching
COPY renv.lock .
COPY .Rprofile .
COPY renv/activate.R renv/

# Restore exact package dependencies
RUN R -e "renv::restore()"

# Copy application source code
COPY . .

# Run the pipeline
CMD ["Rscript", "main.R"]