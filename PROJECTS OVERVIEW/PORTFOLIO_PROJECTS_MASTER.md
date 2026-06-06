# ?? Master Portfolio Projects Catalog

*A comprehensive, systematically generated index of all engineering projects, research works, and prototypes.*

## ?? Executive Summary
- **Total Projects Detected:** 74
- **Total Technologies Mastered:** 12
- **Primary Domains:** Artificial Intelligence & Machine Learning, Web Development, Data Science & Analytics

### Category Distribution
- **Artificial Intelligence & Machine Learning:** 66 projects
- **Web Development:** 4 projects
- **Data Science & Analytics:** 2 projects
- **Software Engineering:** 1 projects
- **Research & Academic Projects:** 1 projects

### Top Technologies
Python (43), HTML (38), JavaScript (28), Node.js (25), CSS (21), TypeScript (14), General Programming (11), Jupyter Notebook (9), C/C++ (7), Docker (5)

## ⭐ Featured Projects
- **[A Recursively Adaptive Meta-Plasticity Framework with Lyapunov-Constrained Stability](./research paper 1)**: [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/) [![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
- **[AI Architecture & System Design Repositories](./AI)**: This repository contains technical reports, proposals, and design reviews detailing big-data systems, event-driven web applications, and neural network pipelines.
- **[AQI Scraper - Air Quality Data Harvester](./HACKATHON DATA)**: Environmental analytics pipelines require reliable, real-time data feeds, but public API portals are often rate-limited, fail frequently, or return inconsistent telemetry.
- **[AnimeFaceReplace - Face Mesh Overlay Tool](./ayanakoji face replacing)**: Real-time graphic overlays on human faces often suffer from alignment drift, lag, and poor perspective mapping when faces rotate.
- **[Anti-Gravity Bot - Quant Trading Orchestrator](./TRADING BOT)**: Building algorithmic trading software requires strict separation between data fetching, feature calculation, strategy evaluation, and order placement.

## ?? Project Details

### ??️ Artificial Intelligence & Machine Learning
---

#### A Recursively Adaptive Meta-Plasticity Framework with Lyapunov-Constrained Stability

**Elevator Pitch:** *[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/) [![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)*

**Portfolio Tags:** `Advanced` | `Research` | `Artificial Intelligence & Machine Learning`

**Technologies:** Docker, Python

**Repository Path:** `./research paper 1`

##### Overview
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)

##### Problem Solved
Addressed technical challenges in developing robust systems for research paper 1.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### AI Architecture & System Design Repositories

**Elevator Pitch:** *This repository contains technical reports, proposals, and design reviews detailing big-data systems, event-driven web applications, and neural network pipelines.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, Jupyter Notebook, HTML, JavaScript, Node.js, CSS, TypeScript

**Repository Path:** `./AI`

##### Overview
This repository contains technical reports, proposals, and design reviews detailing big-data systems, event-driven web applications, and neural network pipelines. Rather than simple code blocks, this collection illustrates production-level system designs, database schemas, and ML model evaluations, serving as a blueprint for big-tech and enterprise software architectures.

##### Problem Solved
Addressed technical challenges in developing robust systems for AI.

##### Core Features
* **Systems Architecture Diagrams**: Includes technical designs detailing data processing pipelines, database normalization layouts, and RAG architectures.
* **Model Evaluations**: Analyzes neural network model parameterizations, metrics comparisons, and deployment limits.
* **Event-Driven App Proposals**: Documents multi-user platform designs featuring low-latency pub/sub message brokers and load-balanced microservices.

##### Key Highlights
Unlike standard code repositories, this project acts as a portfolio of architectural thinking and infrastructure designs. It showcases documentations on database systems design (DBMS), big data management (BDM), machine learning foundations (MLF), and community aggregation networks, demonstrating product strategy and systems scalability planning.

<br/>


#### AQI Scraper - Air Quality Data Harvester

**Elevator Pitch:** *Environmental analytics pipelines require reliable, real-time data feeds, but public API portals are often rate-limited, fail frequently, or return inconsistent telemetry.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./HACKATHON DATA`

##### Overview
Environmental analytics pipelines require reliable, real-time data feeds, but public API portals are often rate-limited, fail frequently, or return inconsistent telemetry. `AQI Scraper` is a data harvesting pipeline designed to query the OpenAQ API, retrieve measurements across multiple Indian monitoring stations, parse API responses, and compile them into structured datasets, demonstrating data collection engineering.

##### Problem Solved
* **Rate Limits and Connection Timeouts**: Public APIs frequently rate-limit clients or timeout when querying multiple stations. The scraper addresses this by isolating individual request loops: if an API call fails or times out, the error is caught, the event is logged, and the script immediately moves to the next station, ensuring complete database runs.

##### Core Features
* **Automated Station Iteration**: Parses a local index (`indian_stations.json`) containing metadata for all Indian monitoring stations.
* **API Rate-Limit Handling**: Employs non-blocking exception handling to skip failed stations, preventing script crashes during API outages.
* **Structured Data Exporting**: Transforms API response payloads into a single, structured dataset (`indian_measurements.json`).
* **Environment Configuration**: Employs API authentication keys mapped via dynamic request headers.

##### Key Highlights
`AQI Scraper` is built for operational reliability. By reading from a structured list of station IDs, it isolates API failures to specific locations, allowing the scraper to continue processing the rest of the queue. The resulting JSON dataset maps out clean station locations, measurements, and timestamps.

<br/>


#### AnimeFaceReplace - Face Mesh Overlay Tool

**Elevator Pitch:** *Real-time graphic overlays on human faces often suffer from alignment drift, lag, and poor perspective mapping when faces rotate.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./ayanakoji face replacing`

##### Overview
Real-time graphic overlays on human faces often suffer from alignment drift, lag, and poor perspective mapping when faces rotate. `AnimeFaceReplace` provides a high-fidelity face overlay tool. Using OpenCV, it captures webcam video streams, detects faces via dlib or MediaPipe Face Mesh, maps 68 spatial landmarks, and overlays an anime character mask, applying rotation offsets and perspective warps in real time.

##### Problem Solved
* **Overlay Drifting on Face Rotations**: 2D graphic overlays look flat and drift when users turn their heads. The tool solves this by calculating rotation angles from facial landmark ratios (e.g. nose-to-jaw distances), warping the overlay image using affine transformations to match the user's pose, ensuring a stable fit.

##### Core Features
* **Facial Landmark Mapping**: Details 68 landmark coordinates using dlib and MediaPipe Face Mesh (with refined iris tracking).
* **Perspective Warping & Alpha Masking**: Calculates coordinate transformation matrices to rotate, scale, and warp overlays to match the user's pose.
* **Dynamic Face Masking**: Uses alpha channels to blend transparent graphic overlays over live frames.
* **Optimized Video Capturing**: Configures OpenCV preprocessing pipelines to run frames at low latency.

##### Key Highlights
* **3D Mask Modeling**: Import 3D OBJ models and render them over landmarks using OpenGL.
* **Expression Mapping**: Map landmark movements (smiles, blinks) to trigger animations on the overlay mask.
* **Webcam Virtual Driver**: Output the composited video feed as a virtual camera source for Zoom or Discord.

<br/>


#### Anti-Gravity Bot - Quant Trading Orchestrator

**Elevator Pitch:** *Building algorithmic trading software requires strict separation between data fetching, feature calculation, strategy evaluation, and order placement.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python

**Repository Path:** `./TRADING BOT`

##### Overview
Building algorithmic trading software requires strict separation between data fetching, feature calculation, strategy evaluation, and order placement. Coupling these components leads to system instability and capital loss. `Anti-Gravity Bot` implements a modular quantitative trading framework. It fetches market data via `yfinance`, computes indicators in Pandas, evaluates Pine-Script style crossover strategies, passes orders through a strict risk manager, and logs executions to a virtual ledger, providing a framework for algorithmic trading.

##### Problem Solved
* **Accurate Ledger Accounting**: Simple trading simulators often track only cash balances and fail to calculate mark-to-market equity during open trades. The `PaperBroker` solves this by tracking asset positions, calculating dynamic equity (Cash + Position Value) based on latest ticker prices, and computing dynamic stop-losses, preventing inaccurate backtesting.

##### Core Features
* **Modular Domain Architecture**: Clean separation of packages: `data_fetcher`, `indicators`, `ema_strategy`, `risk_manager`, and `paper_broker`.
* **Professional Virtual Ledger**: The `PaperBroker` manages capital balances, equity, position values, and unrealized/realized P&L in CSV logs.
* **Capital Protection Risk Gate**: Implements a `RiskManager` enforcing risk per trade limits, daily drawdown limits, and consecutive loss cooldowns.
* **Technical Analysis Engine**: Calculates EMA crossover spreads, RSI, MACD, Bollinger Bands, and ATR using the `ta` library.
* **Training Data Recorder**: Logs technical features and trade outcomes to CSV, building clean datasets for future ML models.

##### Key Highlights
`Anti-Gravity Bot` is built for capital preservation. Before an order is sent to the execution engine, it must pass through the `RiskManager` gate. If the trade risks more than the configured percentage of capital, or if the daily loss threshold is breached, the trade is blocked, simulating professional risk management.

<br/>


#### AutoMail - RAG Email & Browser Automation Engine

**Elevator Pitch:** *Managing corporate email channels manually introduces high operational overhead, with response delays directly impacting customer satisfaction.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./automation system`

##### Overview
Managing corporate email channels manually introduces high operational overhead, with response delays directly impacting customer satisfaction. `AutoMail` provides a production-grade email automation engine. It automates Chrome interactions, downloads Gmail attachments, indexes content in a local vector database, and generates context-aware email responses using LLM prompts, providing a framework for autonomous customer service.

##### Problem Solved
* **Attachment Serialization and Formatting**: Email attachments come in various formats (PDFs, images, Excel), making text extraction difficult. The pipeline addresses this by deploying specialized extraction modules that convert raw document layouts into clean text blocks before vectorization, ensuring data consistency.

##### Core Features
* **Chrome Browser Driver**: Automates browser navigation, content extraction, and page interactions.
* **Gmail Attachment Ingestion**: Automates Gmail attachment downloads and processes files.
* **Vector DB & Embeddings Engine**: Indexes parsed email text and attachments into a local vector database for semantic search.
* **LLM Connector**: Generates personalized email replies using structured prompt templates.
* **Structured Logging & Retries**: Employs robust logging and error recovery across automation runs.

##### Key Highlights
* **Multi-Channel Automation**: Expand pipelines to support Slack, Discord, and CRM interfaces.
* **Human-in-the-Loop Review**: Build a review dashboard allowing managers to approve drafts before sending.
* **Observed Sentiment Classification**: Classify incoming emails by urgency and sentiment to prioritize replies.

<br/>


#### BBC news NLP Sequential Classifier

**Elevator Pitch:** *Parsing and categorizing large flows of textual news feeds is computationally expensive for editorial teams.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./BBC classification`

##### Overview
Parsing and categorizing large flows of textual news feeds is computationally expensive for editorial teams. Standard keyword matching is too fragile to capture context. `BBC News Classifier` implements a deep learning pipeline that preprocesses raw documents, extracts sentiment values, models word frequencies, and trains a sequential neural network (Keras) to classify documents into categorical classes (e.g., tech, business, politics), illustrating document intelligence processing at scale.

##### Problem Solved
* **Dimensionality Explosion & Sparse Vectors**: High-vocabulary datasets result in extremely sparse matrices that slow down neural network training. The pipeline implements strict token pruning (filtering stopwords and stemming word roots) before vector transformation, reducing input features to a dense, computationally efficient matrix.

##### Core Features
* **Multi-Stage Text Preprocessing**: Integrates regex token cleaning, stopword removal, and word stemming via NLTK (PorterStemmer).
* **VADER Sentiment Indexing**: Calculates sentiment polarity scores for text segments, injecting behavioral metrics into the feature pipeline.
* **Sequential Neural Network**: Implements a Keras-based deep neural network with multiple dense layers optimized for multi-class classification.
* **Exploratory Data Visualizations**: Generates word clouds and data distribution grids using Seaborn and Plotly.

##### Key Highlights
This pipeline combines lexical NLP techniques (stemming, tokenizing) with emotional sentiment profiling (VADER) and sequential deep learning models (Keras). By feeding structured text characteristics and sentiment dimensions into a deep neural net, the model learns complex vocabulary patterns, making it highly robust against shifts in writing style compared to basic Naive Bayes models.

<br/>


#### BDM Project - Business Intelligence & Database Engineering

**Elevator Pitch:** *Modern business operations generate massive amounts of unstructured transaction data that remains siloed in incompatible formats.*

**Portfolio Tags:** `Intermediate` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./BDM PROJ`

##### Overview
Modern business operations generate massive amounts of unstructured transaction data that remains siloed in incompatible formats. `BDM Project` resolves this by proposing structured database schemas, data cleansing pipelines, and business intelligence models. This analysis establishes clean ETL workflows that transform raw spreadsheet transactions into highly structured database models, enabling operations analytics.

##### Problem Solved
Addressed technical challenges in developing robust systems for BDM PROJ.

##### Core Features
* **Schema Design and Normalization**: Defines clean relational database structures (schema.sql) mapping entities, keys, and relational constraints.
* **Data Cleansing Pipelines**: Outlines structured cleaning processes for complex datasets to remove duplicates, null fields, and inconsistencies.
* **BI Report Proposals**: Provides business intelligence summaries analyzing transactional performance, market segmentation, and database integrity.

##### Key Highlights
This project is an advanced analysis of business data structures, focusing on the interface between raw database engineering and enterprise strategy. By outlining normalized relational schemas and data cleansing strategies, it bridges the gap between data warehousing and business-level analytics.

<br/>


#### Bhoomi AI - Agricultural RAG Campaign Platform

**Elevator Pitch:** *Agricultural marketing campaigns are often inefficient because they distribute generic advertisements to diverse regional farming segments without accounting for local crop profiles, weather variations, or soil parameters.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Node.js, HTML, Python, JavaScript

**Repository Path:** `./SYGENTA HACKATHON`

##### Overview
Agricultural marketing campaigns are often inefficient because they distribute generic advertisements to diverse regional farming segments without accounting for local crop profiles, weather variations, or soil parameters. `Bhoomi AI` solves this by deploying a RAG-powered campaign targeting platform. It stores farmer profile metrics in ChromaDB, queries the vectors semantically via LangChain, and orchestrates LLM agents (FastAPI backend) to draft crop-specific marketing content tailored to regional variables, serving as a template for targeted agricultural RAG systems.

##### Problem Solved
* **Semantic Retrieval Precision**: Naive vector searches often retrieve irrelevant profiles if queries contain conflicting crop names. The pipeline resolves this by implementing hybrid metadata filtering, restricting the ChromaDB query search space to specific geographic locations before running vector computations.

##### Core Features
* **ChromaDB Vector Retrieval**: Indexes and retrieves multi-dimensional farmer profiles based on semantic search queries.
* **LangChain Agent Orchestration**: Configures generative marketing agent loops that draft personalized campaign copy using crop, soil, and weather variables.
* **FastAPI Backend Services**: Implements asynchronous REST endpoints serving campaign stats, profile search, and model logs.
* **Vite React Dashboard**: An interactive frontend dashboard showing campaign outcomes, user segments, and real-time drafts.

##### Key Highlights
`Bhoomi AI` is built on a structured vector schema. Instead of just querying text, it embeds numeric and categorical farmer parameters (e.g., location, crop type, acreage) in ChromaDB, combining semantic vector queries with relational filters. This guarantees that generated copy is contextualized to local farming constraints, avoiding generic text outputs.

<br/>


#### Buddhi Core - Enterprise RAG & Transformer Orchestrator

**Elevator Pitch:** *Deploying Large Language Models at scale in enterprise environments requires robust asynchronous API gateways, structured database schemas, and clean model routing layers.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Docker, Python, HTML, JavaScript, Node.js, CSS, TypeScript

**Repository Path:** `./MIROFISH ADVANCED`

##### Overview
Deploying Large Language Models at scale in enterprise environments requires robust asynchronous API gateways, structured database schemas, and clean model routing layers. Simple wrappers fail under heavy parallel request loads. `Buddhi Core` (under the Mirofish Advanced module) is a production-ready RAG and Transformer orchestrator. It manages user requests via FastAPI, processes vector data asynchronously using SQLAlchemy, runs Alembic migrations, and pipelines prompts to cloud-hosted Nvidia models (e.g., Llama-3.3-70b-instruct), providing a scalable backend for corporate knowledge retrieval.

##### Problem Solved
* **Asynchronous Transaction Failures**: Under heavy concurrent API calls, synchronous database clients block threads, causing timeouts. Switching the codebase to SQLAlchemy async sessions with asyncpg drivers allowed the API to scale to thousands of concurrent requests without blocking.

##### Core Features
* **Asynchronous Database Pipeline**: Implements async database queries using SQLAlchemy with `asyncpg` drivers and Alembic migrations.
* **Model Routing Proxy**: Interfaces with Nvidia API gateways to handle instruction model prompts with automatic retry configurations.
* **Training and Transformer Containers**: Outlines Docker configurations (`Dockerfile.training` and `Dockerfile.transformer`) to deploy model nodes independently.
* **Robust Test Coverage**: Deploys a comprehensive testing suite (pytest) monitoring core pipelines, API responses, and database transaction states.

##### Key Highlights
`Buddhi Core` is architected for production-grade operations. It utilizes asynchronous database calls to prevent request blocking, separates training containers from model inference interfaces, and includes verification check systems (`verify_keys.py`). The application schema is built to store document vectors, session audits, and RAG contexts with high data integrity.

<br/>


#### Buddhi Deploy - Infrastructure & Operations Gateway

**Elevator Pitch:** *Deploying large AI transformer pipelines introduces complex infrastructure requirements, including Redis memory caches, CUDA environments, and Docker container clusters.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./mirofish next level`

##### Overview
Deploying large AI transformer pipelines introduces complex infrastructure requirements, including Redis memory caches, CUDA environments, and Docker container clusters. `Buddhi Deploy` provides deployment automation tools. It maps settings schemas (.claude configurations), verifies cache nodes, and manages container operations, automating the deployment of the Buddhi Core platform.

##### Problem Solved
Addressed technical challenges in developing robust systems for mirofish next level.

##### Core Features
* **System Operations Settings**: Structures platform rules for file renames and testing.
* **Redis Connection Validator**: Inline verification tools confirming in-memory cache states.
* **Multi-Container Operations**: Orchestrates database, training, and model containers.

##### Key Highlights
* **Kubernetes Manifests**: Generate Kubernetes files to support distributed container environments.
* **Prometheus Observability**: Integrate metric monitors to track transformer performance.

<br/>


#### Calyco Strategy - Digital Content Proposals

**Elevator Pitch:** *Developing content strategies for modern digital brands requires structuring distribution channels, analyzing market opportunities, and mapping out content pipelines.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./calyco`

##### Overview
Developing content strategies for modern digital brands requires structuring distribution channels, analyzing market opportunities, and mapping out content pipelines. `Calyco Strategy` compiles marketing proposals, platform audits, and workflow designs, organizing content calendars and tracking performance metrics.

##### Problem Solved
Addressed technical challenges in developing robust systems for calyco.

##### Core Features
* **Content Pipeline Designs**: Structures content creation and publishing workflows across digital channels.
* **Channel Distribution Strategies**: Audits digital platforms to optimize audience reach.
* **Operations Frameworks**: Maps out team roles and publishing schedules.

##### Key Highlights
* **Dynamic Marketing Dashboard**: Build a dashboard to track real-time campaign performance.
* **Automated Publishing API**: Implement scripts to schedule and publish posts directly to platforms.

<br/>


#### CareerPortal Staging - Campus Recruitment Portal

**Elevator Pitch:** *This is the staging and R&D directory for the database-driven campus placement platform.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, Jupyter Notebook, HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./intership`

##### Overview
This is the staging and R&D directory for the database-driven campus placement platform. It hosts model structures, registration routes, and admin monitoring dashboards, replicating the core MVC database models to run structural tests and index credentials safely.

##### Problem Solved
Addressed technical challenges in developing robust systems for intership.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### CodeVita - Algorithmic Contest Solutions

**Elevator Pitch:** *Solving performance-critical algorithmic challenges under strict time constraints requires optimized data structures, time-complexity analysis, and clean logic.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./codevita`

##### Overview
Solving performance-critical algorithmic challenges under strict time constraints requires optimized data structures, time-complexity analysis, and clean logic. `CodeVita` compiles Python solutions for competitive programming. These scripts implement advanced algorithms (DFS/BFS, Dijkstra's, dynamic programming memoization, binary searches) to resolve complex computational constraints.

##### Problem Solved
Addressed technical challenges in developing robust systems for codevita.

##### Core Features
* **Graph Algorithms**: Implements optimized graph traversals and shortest-path solvers.
* **Dynamic Programming**: Uses memoization and tabulation to optimize recursive functions.
* **Efficient I/O Handlers**: Deploys fast input/output parsing routines to prevent timeout errors.

##### Key Highlights
* **Automated Test Runner**: Build a shell script to run solution binaries against target input/output test cases.
* **Complexity Benchmarks**: Include runtime profiles comparing execution times across different algorithms.

<br/>


#### CommunityPulse - Event Orchestration Portal

**Elevator Pitch:** *Organizations hosting multiple public events struggle to manage user registrations, track seat capacities, and publish calendars.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python

**Repository Path:** `./hackathon IIT M x odoo`

##### Overview
Organizations hosting multiple public events struggle to manage user registrations, track seat capacities, and publish calendars. Fragmented tools lead to overbooking and data inconsistencies. `CommunityPulse` provides a unified event management portal. Built with Flask and SQLAlchemy, it implements relational schemas mapping users and events, deploys WTForms to validate user inputs, and renders an interactive web interface for event discovery and booking.

##### Problem Solved
* **Validation Anomalies in Date Parsing**: Form inputs for event dates often crash database models due to format discrepancies. The system addresses this by configuring form fields using `DateTimeField` constraints and converting inputs into Python `datetime` objects before database ingestion, preventing query failures.

##### Core Features
* **Relational Schema Mapping**: Employs SQLAlchemy to map `User` and `Event` tables, implementing foreign key bindings and dynamic backreferences.
* **WTForms Input Validation**: Secures routes with structured forms (`RegistrationForm`, `LoginForm`, `EventForm`), enforcing data rules and email validations.
* **State-Preserving Session Manager**: Uses Flask Sessions to manage user logins and restrict booking routes to verified accounts.
* **Dynamic Query Ingestion**: Queries databases dynamically to list events by date and category.

##### Key Highlights
* **Capacity Limits & Waitlists**: Add a transaction-safe seat counter to prevent overbooking and queue waitlisted users.
* **Email Ticket Dispatcher**: Integrate email clients to automatically send confirmation tickets with QR codes.
* **Real-time Map Search**: Map event coordinates using Leaflet.js to allow location-based event searches.

<br/>


#### CommunityPulse Client - React TS Frontend Dashboard

**Elevator Pitch:** *Fragmented event systems make discovery and booking difficult due to heavy, non-responsive interfaces.*

**Portfolio Tags:** `Advanced` | `Research` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./t7_hackathon`

##### Overview
Fragmented event systems make discovery and booking difficult due to heavy, non-responsive interfaces. `CommunityPulse Client` provides a responsive frontend dashboard. Built with React and TypeScript, it structures grid layouts, card components (`EventCard.tsx`), and event filters, delivering an analytics-oriented discovery dashboard.

##### Problem Solved
Addressed technical challenges in developing robust systems for t7_hackathon.

##### Core Features
* **Vite React TS Build System**: Optimized bundler configurations featuring strict TypeScript types across component boundaries.
* **Modular Component Grids**: Implements card components (`EventCard.tsx`) to display event details.
* **Tailwind Layout Design**: Responsive page templates utilizing utility-first CSS classes.

##### Key Highlights
* **Live API Sync**: Connect the frontend to a Flask/PostgreSQL event backend.
* **Interactive Map**: Integrate Leaflet.js to allow location-based event searches.

<br/>


#### CovidETL - Global Time Series Data Pipeline

**Elevator Pitch:** *Unprocessed epidemiologic timeseries data is notoriously noisy, inconsistent, and fragmented across disparate global repositories.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Jupyter Notebook

**Repository Path:** `./ETL-Project-master`

##### Overview
Unprocessed epidemiologic timeseries data is notoriously noisy, inconsistent, and fragmented across disparate global repositories. `CovidETL` implements a clean data engineering pipeline that automates the extraction of global COVID-19 datasets, executes relational data cleaning routines in Pandas, and loads the structured data into a PostgreSQL data warehouse, establishing an analytics-ready database.

##### Problem Solved
* **Reshaping Wide Time Series Data**: Raw timeseries files format dates as columns, which violates relational database structures (1NF). The transformation notebook solves this by using the pandas `melt` function, folding wide date columns into dynamic rows (`Date` and `Value`), and indexing them by Location, enabling direct relational SQL analysis.

##### Core Features
* **Multi-Phase Pipeline Design**: Separates execution stages into dedicated Jupyter notebooks: `Extract.ipynb`, `Transform.ipynb`, and `Load.ipynb`.
* **Pandas Transformation Layer**: Standardizes schema columns, replaces null values, aggregates country regions, and converts wide tables into long database formats.
* **PostgreSQL Schema Mapping**: Defines relational constraints, foreign keys, and primary indices (`schema.sql`) to guarantee data integrity.
* **Exploratory Data Visualizations**: Generates analysis plots (e.g. confirmed cases, recovered rates, and death distributions).

##### Key Highlights
`CovidETL` does not simply copy files. It transforms wide-format timeseries files into database-ready tables. It maps out an Entity-Relationship Diagram (ERD) defining relational connections, and enforces clean database ingestion rules to prevent data duplication.

<br/>


#### Delinquency Classifier - Credit Risk ML Pipeline

**Elevator Pitch:** *Financial institutions struggle to identify customer credit card delinquencies early because transaction records are highly unbalanced, with default cases representing only a tiny fraction of total accounts.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./TATA INTERSHIP`

##### Overview
Financial institutions struggle to identify customer credit card delinquencies early because transaction records are highly unbalanced, with default cases representing only a tiny fraction of total accounts. Machine learning models trained on unbalanced datasets default to predicting the majority class, missing high-risk cases. `Delinquency Classifier` implements a machine learning pipeline that applies SMOTE (Synthetic Minority Over-sampling Technique) to balance datasets and evaluates Random Forest and XGBoost classifiers to predict delinquencies, improving risk detection.

##### Problem Solved
* **Overfitting from Synthetic Leakage**: Running SMOTE before cross-validation splitting causes data leakage, artificially inflating model accuracy. The pipeline solves this by implementing SMOTE within structured cross-validation pipelines (imblearn Pipeline), ensuring synthetic data is generated only on training folds and never on validation folds.

##### Core Features
* **SMOTE Over-sampling Pipeline**: Addresses class imbalance by generating synthetic minority-class vectors before model training.
* **XGBoost Risk Modeling**: Builds and tunes gradient boosting classifiers to maximize recall on delinquent accounts.
* **Random Forest Benchmarking**: Compares Random Forest classifiers against XGBoost to evaluate metrics (Precision, Recall, ROC-AUC).
* **Exploratory Analytics Reports**: Includes detailed data analysis summaries mapping risk factors and feature importances.

##### Key Highlights
This project focuses on model auditing for financial operations. Instead of optimizing for overall accuracy, it optimizes for **Recall** on minority classes (the delinquent accounts), minimizing financial loss for the lender. The pipeline uses cross-validation splits to verify that synthetic samples do not leak into evaluation folds.

<br/>


#### DevRegistry - Open Source Settings

**Elevator Pitch:** *This repository indexes developer workspace configurations, VSCode settings schemas, and Terraform state exclusion tables, maintaining clean environments across developer nodes.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, HTML, JavaScript, Node.js, TypeScript, Go

**Repository Path:** `./open source projects`

##### Overview
This repository indexes developer workspace configurations, VSCode settings schemas, and Terraform state exclusion tables, maintaining clean environments across developer nodes.

##### Problem Solved
Addressed technical challenges in developing robust systems for open source projects.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### Dragon Companion - Flutter Mobile Client

**Elevator Pitch:** *Developing mobile utilities that remain consistent across Android, iOS, and Web requires structured state managers and modular layout engines.*

**Portfolio Tags:** `Intermediate` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Java, HTML

**Repository Path:** `./dragon`

##### Overview
Developing mobile utilities that remain consistent across Android, iOS, and Web requires structured state managers and modular layout engines. `Dragon Companion` provides a cross-platform mobile client built on Flutter. It structures view files, hooks into plugin interfaces, and manages compilation outputs, delivering a lightweight dashboard for systems integrations.

##### Problem Solved
Addressed technical challenges in developing robust systems for dragon.

##### Core Features
* **Cross-Platform Compilation**: Structures Dart configurations compiling to native mobile code and Web builds.
* **Modular View Layouts**: Defines reusable widgets and UI containers.
* **System Plugins Mapping**: Tracks package and dependency configurations in `pubspec.yaml`.

##### Key Highlights
* **REST API Connector**: Connect UI layouts to remote server APIs.
* **SQLite Local Caching**: Implement local SQLite storage (Hive or sqflite) to support offline states.

<br/>


#### EchoSoul - Full-Stack Generative AI Companion Platform

**Elevator Pitch:** *Building conversational companions with LLMs requires managing session history, persistent memories, and custom character prompt templates.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Node.js, HTML, JavaScript

**Repository Path:** `./ECHOSOUL`

##### Overview
Building conversational companions with LLMs requires managing session history, persistent memories, and custom character prompt templates. Simple APIs lose state, leading to disjointed agent conversations. `EchoSoul` introduces a full-stack architecture using Node/Express, Supabase, and the Groq SDK. By mapping user sessions, character definitions, and message histories to PostgreSQL, the system provides persistent, low-latency, context-aware dialogues.

##### Problem Solved
* **Database Connection Pools & History Overhead**: Loading large conversation histories on every chat request introduces significant database query latencies. The service solves this by implementing structured query limits, retrieving only the latest context window (e.g. last 15 messages) and utilizing Supabase indices on session IDs, keeping response generation under 500ms.

##### Core Features
* **Persistent Session Orchestration**: Bridges Node.js Express routers with Supabase client wrappers, managing active chat states.
* **Relational Message Schema**: Implements structured tables (`chats` and `messages`) to log user-agent interactions for conversational retrieval.
* **Groq API Integrations**: Interfaces with Groq completions endpoint, passing system prompts and message histories to models.
* **Security & Authentication Layer**: Deploys server-side token validation using JWT and password hashing via bcryptjs.

##### Key Highlights
`EchoSoul` separates character data (`characters.json`) from the core state engine, allowing developers to register new companion personas without restarting services. It compiles chat history dynamically on every request, formatting conversation logs into OpenAI-compatible message lists, preventing model drift while maintaining low API latencies.

<br/>


#### EduDash - EdTech Analytics Frontend Application

**Elevator Pitch:** *Educators and course administrators often struggle to track student engagement, learning analytics, and course progress due to fragmented, non-interactive reporting interfaces.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, C/C++, HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./PRODUCT1`

##### Overview
Educators and course administrators often struggle to track student engagement, learning analytics, and course progress due to fragmented, non-interactive reporting interfaces. `EduDash` provides a responsive, analytics-oriented dashboard. Built with React, TypeScript, and Vite, it structures student tracking panels, visualizes course performance using Recharts, and implements clean client routing, delivering a modern analytics interface.

##### Problem Solved
* **Chart Reflow and Layout Distortion**: Interactive SVG charts frequently break page alignments when window sizes change. The dashboard resolves this by wrapping charts in responsive containers, recalculating chart scales on window resize events to maintain dashboard alignment.

##### Core Features
* **Interactive Charting Engine**: Uses Recharts to render student progress metrics and course engagement stats.
* **Modular Router Configuration**: Configures React Router to manage dashboard views and navigation states.
* **Tailwind Layout Design**: Implements fully responsive dashboards utilizing Tailwind CSS.
* **Clean Components Structure**: Separates layout panels, charts, and table components to ensure code reusability.

##### Key Highlights
* **Backend API Integration**: Connect the dashboard to a live Flask or Node.js backend.
* **Real-time WebSockets**: Integrate WebSockets to stream student event logs in real time.
* **PDF Report Generator**: Add client-side PDF export features for administrators.

<br/>


#### EmoPet - Bio-Interactive Companion System

**Elevator Pitch:** *This folder contains the system specifications and product design proposals for `EmoPet` (an emotional AI companion).*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./emopet`

##### Overview
This folder contains the system specifications and product design proposals for `EmoPet` (an emotional AI companion). It maps out hardware requirements, user interaction flows, and AI behaviors, bridging the gap between product strategy and engineering execution.

##### Problem Solved
Addressed technical challenges in developing robust systems for emopet.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
* **Hardware Prototyping**: Build the initial sensor interface using Raspberry Pi and Python.

<br/>


#### Experimental Archive - R&D Codebase Museum

**Elevator Pitch:** *This directory serves as a developmental archive.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python, JavaScript, CSS

**Repository Path:** `./failed projects`

##### Overview
This directory serves as a developmental archive. It stores old feature versions, experimental scripts, and sandbox codebases that were compiled during portfolio R&D, serving as a reference library for software design iterations.

##### Problem Solved
* **Session Leakage and Transaction Errors**: Concurrent user requests can cause SQLite connection locks and session leakage. The app solves this by registering teardown handlers (`@app.teardown_appcontext`), removing the scoped session automatically after every request, preventing database locks.

##### Core Features
* **Relational Database Design**: Employs SQLAlchemy to map `users`, `recruiter_profiles`, `student_profiles`, and `job_drives` tables with foreign key constraints.
* **Role-Based Access Guards**: Implements server-side route decorators (`@login_required`, `@role_required`) to restrict access based on user credentials.
* **Automatic Database Seeding**: Configures seed scripts (`database.py`) that verify and initialize default admin accounts.
* **Multi-user Dashboard Panels**: Structured Jinja2 layouts managing recruitment metrics, student profiles, and application statuses.
* **Secure Credentials Hashing**: Imploys SHA256 hashing via Werkzeug security wrappers for user password protection.

##### Key Highlights
`PlacementPortal` is built around relational integrity. If a job drive is deleted, SQLAlchemy cascade deletion rules update the associated student applications automatically. The application forms check eligibility thresholds (e.g. cgpa and backlog limits) before allowing students to submit applications, ensuring data accuracy.

<br/>


#### Git Configurations - Workspace Settings

**Elevator Pitch:** *This folder contains target Git ignore files and repository settings, maintaining clean workspace files and preventing local virtual environments from leaking into public repositories.*

**Portfolio Tags:** `Beginner/Prototype` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./github`

##### Overview
This folder contains target Git ignore files and repository settings, maintaining clean workspace files and preventing local virtual environments from leaking into public repositories.

##### Problem Solved
Addressed technical challenges in developing robust systems for github.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### GradientRegressor - Logistic Regression from Scratch

**Elevator Pitch:** *Relying entirely on scikit-learn abstracts the underlying mathematical mechanics of ML algorithms, making it difficult to debug convergence anomalies or optimize custom loss functions.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, Jupyter Notebook

**Repository Path:** `./project4`

##### Overview
Relying entirely on scikit-learn abstracts the underlying mathematical mechanics of ML algorithms, making it difficult to debug convergence anomalies or optimize custom loss functions. `GradientRegressor` implements a binary logistic regression pipeline from scratch. Written in Python using NumPy, it handles data normalization (Min-Max scaling), implements the Sigmoid activation, runs gradient descent optimizations, and plots loss curves, validating numerical classification mechanics.

##### Problem Solved
* **Numerical Overflow in Sigmoid Functions**: Large negative inputs in standard sigmoid equations cause floating-point overflows. The numerical core solves this by clipping input values to a safe range before exponentiation, ensuring training stability.

##### Core Features
* **Gradient Descent Optimizer**: Implements vector-based weight and bias updates to minimize loss functions.
* **Sigmoid Activation Layer**: Computes non-linear probability boundaries from raw input vectors.
* **Min-Max Data Scaler**: Standardizes and scales feature values to accelerate model convergence.
* **Matplotlib Loss Tracker**: Generates real-time charts plotting loss reduction across training runs.

##### Key Highlights
* **Multinomial Softmax Classifier**: Expand the model to support multi-class classification using Softmax.
* **L1/L2 Regularization**: Add Lasso and Ridge penalties to the gradient update equations to prevent overfitting.
* **Stochastic Gradient Descent**: Implement SGD to train on small batches, optimizing computation speeds.

<br/>


#### HDL-PID - Digital PID Controller Model & Simulation

**Elevator Pitch:** *Testing hardware designs (like PID controllers) on physical FPGAs or microcontrollers makes debugging complex feedback loops slow and difficult.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, C/C++

**Repository Path:** `./EEKSHI PROJECT`

##### Overview
Testing hardware designs (like PID controllers) on physical FPGAs or microcontrollers makes debugging complex feedback loops slow and difficult. `HDL-PID` implements a co-design system. The core controller is written in synthesis-ready Verilog (`pid_dualwheel.v`), while the simulation, validation, and testbench generation are managed in Python using `MyHDL`. This allows engineers to run high-speed hardware-level simulations, verify signals, and generate VCD wave outputs before deployment.

##### Problem Solved
* **PWM Jitter and Reset Synchronization**: In digital hardware controllers, improper clock alignments during resets can cause transient voltages that damage motor drivers. The Verilog module solves this by implementing synchronous active-high resets, immediate counter zeroing, and PWM gate closures during reset states, preventing electrical failures.

##### Core Features
* **Synthesis-Ready Verilog Core**: Defines a parameterized, dual-wheel PID controller using signed 16-bit target inputs and PWM outputs.
* **MyHDL Simulation Framework**: Models digital logic, clock generation, and stimulus blocks in Python, compiling them to target waveforms.
* **VCD Waveform Export**: Generates Value Change Dump (VCD) logs from simulations, enabling visual signal analysis in GTKWave.
* **Co-Simulation Testbenches**: Provides testbench scripts (`tb_pid`) verifying PWM outputs across varying speed targets.

##### Key Highlights
`HDL-PID` bridges the gap between software programming and hardware design. Instead of using complex hardware description environments, it uses Python (`MyHDL`) as a simulation compiler. This enables rapid, script-driven hardware testing, allowing developers to write test suites and verify PID algorithms under varying inputs.

<br/>


#### Instalação do Nuclei

**Elevator Pitch:** *<h1 align="center">   <br>   <a href="https://nuclei.projectdiscovery.io"><img src="static/nuclei-logo.png" width="200px" alt="Nuclei"></a> </h1>*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./nuclei`

##### Overview
<h1 align="center">
  <br>
  <a href="https://nuclei.projectdiscovery.io"><img src="static/nuclei-logo.png" width="200px" alt="Nuclei"></a>
</h1>

##### Problem Solved
Addressed technical challenges in developing robust systems for nuclei.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### JarvisEvolved - Desktop AI Companion Client

**Elevator Pitch:** *Most AI companion apps utilize basic chat screens that lack desktop integration, dashboard analytics, or clean settings interfaces.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./jarvis  new`

##### Overview
Most AI companion apps utilize basic chat screens that lack desktop integration, dashboard analytics, or clean settings interfaces. `JarvisEvolved` provides a modular React client for desktop AI agents. Built with React, Vite, and Tailwind, it integrates Shadcn UI widgets to structure dashboard views, Google OAuth screens, and chat interfaces, establishing a modern UI framework for desktop assistant software.

##### Problem Solved
Addressed technical challenges in developing robust systems for jarvis  new.

##### Core Features
* **Shadcn UI Widget Grid**: Deploys modern dashboard grids displaying connection logs, assistant statuses, and controls.
* **Google OAuth Integration**: Configures client-side authentication screens (`GoogleAuth.tsx`) to manage user profiles securely.
* **Vite React TS Build System**: Optimized bundler configurations featuring strict TypeScript types across component boundaries.

##### Key Highlights
* **WebSocket Integration**: Connect the frontend to a local Node.js server via WebSockets to stream voice telemetry.
* **Dynamic Theme Engines**: Add dark mode layouts matching futuristic desktop control panels.

<br/>


#### LockVision - IoT Face Recognition Access Controller

**Elevator Pitch:** *Keycard and PIN-based door security systems are vulnerable to credential sharing and physical theft.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, Jupyter Notebook, HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./cnn face recogniasaiton`

##### Overview
Keycard and PIN-based door security systems are vulnerable to credential sharing and physical theft. Traditional face recognition systems are often computationally heavy and run disconnected from physical locks and monitoring logs. `LockVision` implements a secure, IoT-connected facial access controller. It runs real-time facial recognition via OpenCV, matches facial embeddings against database signatures, records transactions in an SQLite ledger, and dispatches lock/unlock payloads to physical relays via the MQTT protocol, providing an end-to-end IoT security system.

##### Problem Solved
* **API Bottlenecks and Video Stream Lag**: Continuous facial embedding comparison on high-resolution frames slows down the server API. The system solves this by resizing video frames (scaling down to 25%) during processing, running comparison logic only on active face detections, and enforcing a 3-second lock cooldown, maintaining a responsive video feed.

##### Core Features
* **Facial Embedding Comparator**: Uses the `face_recognition` library to extract facial vectors and calculate distances against registered users.
* **MQTT Telemetry Client**: Deploys a background MQTT publisher to transmit door-state payloads (`lock/unlock`) to microcontrollers (ESP32/Raspberry Pi) over local brokers.
* **ACID SQLite Access Ledger**: Implements a structured database schema logging name, timestamps, access decisions, and model confidence scores.
* **React + TS Access Log client**: Includes a frontend client displaying live activity logs and webcam streams.
* **Thread-Safe Camera Lock**: Employs Python threading locks (`camera_lock = threading.Lock()`) to prevent resource conflicts during frame capture.

##### Key Highlights
`LockVision` bridges the gap between machine learning models and hardware-level IoT systems. It features a self-refreshing cache (`refresh_interval = 300`) that automatically reloads user face encodings when new profiles are added to the directory. It enforces custom cooldowns (`recognition_cooldown = 3`) to prevent redundant log writing and duplicate lock commands.

<br/>


#### LogBook - Corporate Activity Journal MVP

**Elevator Pitch:** *Organizations lose critical operational context when internal activity reports and technical notes are siloed across scattered chat channels.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Node.js, HTML, JavaScript, CSS

**Repository Path:** `./company-diary-mvp`

##### Overview
Organizations lose critical operational context when internal activity reports and technical notes are siloed across scattered chat channels. `LogBook` provides a secure, full-stack corporate journal platform. It manages entries via a Node.js Express API, runs text validation, and stores relational records in a Supabase PostgreSQL database, establishing a central knowledge directory for team activities.

##### Problem Solved
* **Database Ingestion Integrity**: Improper text formatting and invalid entries corrupt search indices. The system solves this by deploying validators (`validators.js`) that check string lengths and filter scripts, rejecting invalid payloads before database writes occur.

##### Core Features
* **Relational Schema Migrations**: Employs structured SQL migrations (`001_initial_schema.sql`) to define users, teams, and journal tables.
* **JWT Authentication Gate**: Configures server-side route guards verifying JSON Web Tokens and verifying user records in Supabase.
* **Text Processing Services**: Outlines helper modules (`textProcessing.js`) to parse and tag entry contents.
* **Unified Error Orchestrator**: Implements server-side middlewares mapping validation errors, JWT expirations, and API exceptions.
* **Structured Logger**: Configures winston-based logging for API requests, user IPs, and system errors.

##### Key Highlights
`LogBook` is built for secure corporate environments. The Supabase connection client is configured with service-role privileges that bypass Row-Level Security safely on the server side (`autoRefreshToken: false`, `persistSession: false`), enforcing access rules directly in the API controllers.

<br/>


#### MeshChat - Decentralized P2P Android Messenger

**Elevator Pitch:** *Centralized communication networks fail during natural disasters, in remote locations, or under strict network blockades.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./MeshChat`

##### Overview
Centralized communication networks fail during natural disasters, in remote locations, or under strict network blockades. Standard messaging apps require internet or cellular base stations. `MeshChat` addresses this by establishing a decentralized, local-only P2P communication network. Built natively for Android using Kotlin, it utilizes Bluetooth Classic and Low Energy (BLE) to advertise, discover, and route messages across peer devices. By combining mesh routing algorithms with end-to-end encryption, it provides secure communication without internet connectivity.

##### Problem Solved
* **Socket Failures During Connection Loss**: Mobile devices constantly change physical locations, causing Bluetooth connections to drop. The service addresses this by implementing an automatic reconnection queue: it monitors socket statuses, retries failed handshakes, and queues outgoing messages in the local database, flushing them immediately upon reconnection.

##### Core Features
* **Bluetooth Mesh Controller**: Manages local RFCOMM channel loops, BLE advertisements, and background socket listening threads.
* **End-to-End Encryption (E2EE)**: Implements cryptographic key exchanges and message encrypt/decrypt pipelines using custom Key and Crypto managers.
* **Room SQL Database**: Uses Room library to log local message histories and peer device mappings with ACID compliance.
* **Android Service Integration**: Implements a persistent background service (`BluetoothMeshService`) to maintain network connections when the UI is inactive.
* **Interactive UI Views**: Multi-activity layouts managing peer lists, chat screens, and connection states.

##### Key Highlights
`MeshChat` operates without centralized servers. It implements a P2P routing protocol: when a node receives a message, it verifies the recipient key and propagates the packet across adjacent peers if needed. The local storage handles message states (sent, received, read) offline, and automatically synchronizes history when devices reconnect.

<br/>


#### MeshChat Full - Android Mesh Messenger with Advanced Diagnostics

**Elevator Pitch:** *This repository contains the complete codebase and diagnostics reports for `MeshChat`.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./MeshChat_Full`

##### Overview
This repository contains the complete codebase and diagnostics reports for `MeshChat`. It includes build performance logs, Gradle configs, and the full Kotlin/Java package definitions. The system uses local Bluetooth networks to run peer discovery, end-to-end encrypted packet exchanges, and persistent SQLite database logging, providing a secure, internet-free communications app.

##### Problem Solved
Addressed technical challenges in developing robust systems for MeshChat_Full.

##### Core Features
* **P2P Socket Management**: Implements Bluetooth socket connection pools and data streams.
* **E2EE Cryptography**: Deploys RSA-AES encryption pipelines with secure public-private key managers.
* **Room Database Relational Schema**: Persists messaging threads and contact records locally.
* **Android Gradle Diagnostics**: Includes detailed compilation configurations and performance logs.

##### Key Highlights
This version of MeshChat includes complete compilation profiles and Gradle diagnostic reports. It highlights the full package architecture, database schemas, and background services required to maintain a decentralized messaging network on Android.

<br/>


#### MudletQ - Amazon Q Mudlet Client Integration

**Elevator Pitch:** *Multi-User Dungeon (MUD) clients run in real time and require fast, dynamic reactions.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Docker, Python

**Repository Path:** `./nationsheild`

##### Overview
Multi-User Dungeon (MUD) clients run in real time and require fast, dynamic reactions. Traditional scripts are static and unable to help players write custom triggers or explain game worlds. `MudletQ` solves this by embedding the Amazon Q AI assistant directly into the Mudlet client. Written in Lua, it handles user prompts, configures AWS regions and profiles, and triggers installers, providing real-time AI assistance inside game clients.

##### Problem Solved
Addressed technical challenges in developing robust systems for nationsheild.

##### Core Features
* **Native Mudlet Integration**: Establishes Lua event bindings (`main/amazon_q_main.lua`) to capture client events and display AI assistant outputs.
* **Lua Test Runner**: Includes test suites (`tests/test_amazon_q.lua`) to verify connection integrity and API payload structures.
* **Declarative Module Schema**: Defines configuration schemas (`module.json`) mapping AWS regions, profiles, and logging levels.
* **Automated Installer**: Implements custom installer scripts (`installer/amazon_q_installer.lua`) that configure dependencies.

##### Key Highlights
* **Dynamic Triggers Generator**: Allow Amazon Q to generate and register new Lua client scripts dynamically.
* **Local LLM Fallback**: Add local LLM routers to support offline client assistance.

<br/>


#### MultiBot - Multimodal Conversation & Vision System

**Elevator Pitch:** *Most chatbot interfaces are limited to single-modality text streams, lacking situational awareness or environmental context.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./chatbot`

##### Overview
Most chatbot interfaces are limited to single-modality text streams, lacking situational awareness or environmental context. `MultiBot` introduces a multi-modal agent platform. It coordinates NLP response engines (ChatterBot with SQL storage layers) with real-time webcam computer vision inputs. The CV pipelines track face and eye positions (Haar Cascades for eye contact detection) and hand gesture coordinates (MediaPipe landmarks), establishing a foundation for context-aware digital assistants.

##### Problem Solved
* **Camera Thread Blocking**: Running heavy MediaPipe hand mesh calculations inside the conversational terminal loop halts input capture. The system solves this by running OpenCV frames in an isolated capture loop, writing coordinate states to in-memory buffers that are polled by the main bot loop, preserving interactive execution.

##### Core Features
* **Webcam Gesture Landmark Tracker**: Uses MediaPipe Hands to extract coordinate matrices and calculate Euclidean distances for gesture recognition.
* **Eye-Contact Biometrics**: Integrates OpenCV Haar Cascades to isolate facial regions and detect eye coordinates, logging engagement metrics.
* **SQL Chatbot Storage**: Deploys ChatterBot with `SQLStorageAdapter` configurations to persist trained dialogues in an SQLite database.
* **Dynamic Search Routing**: Integrates Google Search scrapers to dynamically fetch fallback answers for queries outside the local corpus.

##### Key Highlights
`MultiBot` combines conversational NLP with physical vision tracking. Instead of just replying to text, the codebase is structured to hook vision states (e.g. hand coordinates, eye contact logs) directly into conversational logic. The local SQL database maps conversation histories, while the OpenCV capture threads run asynchronously to prevent interface bottlenecks.

<br/>


#### N8N Workflows - Enterprise Automation Systems

**Elevator Pitch:** *Managing digital media pipelines manually introduces significant operational overhead.*

**Portfolio Tags:** `Intermediate` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./N8N`

##### Overview
Managing digital media pipelines manually introduces significant operational overhead. `N8N Workflows` provides JSON workflow definitions for the n8n automation engine. These files automate content processing, trigger YouTube API uploads, and coordinate cross-platform notifications, enabling developer-level workflow automation.

##### Problem Solved
Addressed technical challenges in developing robust systems for N8N.

##### Core Features
* **Visual Content Pipelines**: Outlines structured API endpoints, triggers, and notification nodes.
* **YouTube API Integration**: Automates channel operations and updates video metadata.
* **Declarative JSON Workflows**: Modular JSON configurations compatible with N8N server engines.

##### Key Highlights
* **AI Content Summarization**: Integrate LLM nodes into N8N to automatically write video descriptions and social copy.
* **Multi-Platform Syndication**: Expand workflows to sync uploads to Twitter, LinkedIn, and Discord.

<br/>


#### NDVI Geospatial Remote Sensing Analyzer

**Elevator Pitch:** *Analyzing satellite imagery for environmental changes requires processing multi-spectral raster bands.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python, CSS

**Repository Path:** `./KAGGLE`

##### Overview
Analyzing satellite imagery for environmental changes requires processing multi-spectral raster bands. Traditional GIS software is heavy, expensive, and difficult to automate in data pipelines. `NDVI Geospatial Analyzer` provides a lightweight, script-driven tool that imports spatial raster bands (Red and Near-Infrared), computes normalized vegetation indices, runs threshold segmentation, and converts the resulting raster segments into vector shapefile polygons, enabling automated environmental monitoring.

##### Problem Solved
* **Coordinate Drift During Vectorization**: Converting pixel matrices to vector coordinates can lead to boundary shifts. The exporter resolves this by mapping pixel index coordinates back to spatial metadata (GeoTIFF transforms), ensuring absolute alignment with target map overlays.

##### Core Features
* **Raster Calculations (NDVI)**: Performs array-based computations over Red and Near-Infrared bands to isolate chlorophyll reflections.
* **Vector Polygonization**: Converts threshold-segmented raster grids into vector coordinate shapefiles (SHP) for GIS integration.
* **Spatial Thresholding**: Employs adaptive image thresholding to segment healthy vegetation regions from bare ground.
* **GIS Schema Preservation**: Retains projection and coordinate reference systems (CRS) across raster-to-vector operations.

##### Key Highlights
The toolkit automates the manual GIS drawing process. By combining array processing (NumPy) with geospatial vector boundaries, it transforms pixel-level classifications into geographic shape polygons. This allows engineers to import generated vectors directly into tools like QGIS or ArcGIS without manual digitization.

<br/>


#### OS-Agent R&D - AI Computer Control Workspace

**Elevator Pitch:** *This repository contains the developmental history and experimental prototypes for the computer control AI agent.*

**Portfolio Tags:** `Intermediate` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./automated os`

##### Overview
This repository contains the developmental history and experimental prototypes for the computer control AI agent. It documents the transition from simple coordinate-based clickers to context-aware, OCR-guided multi-tasking agents, illustrating the engineering challenges solved during development.

##### Problem Solved
Addressed technical challenges in developing robust systems for automated os.

##### Core Features
* **Evolution of Agent Architectures**: Contains scripts tracing development stages:
  - `test2.py`: Baseline single-task automation loops.
  - `test4.py` / `test6.py`: Adds multi-task scheduling and context tracking.
  - `test7.py`: Integrates system clipboard support (`pyperclip`).
  - `test12.py`: Implements screen OCR parsing (`pytesseract`) and image captures.
  - `test13.py`: Executes structured JSON action specifications sent by Groq API.
* **Context and State Management**: Implements tracking for active windows (`win32gui`), open programs, and previous actions.
* **Action Specification Parsing**: Translates LLM JSON output (e.g. `mouse_click`, `keyboard_type`) into system events.

##### Key Highlights
* **Visual Bounding Boxes**: Integrate local visual models to identify UI elements without text.
* **Autonomous Task Planner**: Build planning agents that break complex goals into action sequences.

<br/>


#### ParkSync - Flask Vehicle Parking Reservation Portal

**Elevator Pitch:** *Urban vehicle parking is often inefficient due to lack of real-time spot tracking, leading to congestion and manual reservation errors.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python, JavaScript

**Repository Path:** `./vehicle_parking_app`

##### Overview
Urban vehicle parking is often inefficient due to lack of real-time spot tracking, leading to congestion and manual reservation errors. `ParkSync` provides a full-stack vehicle parking spot reservation platform. Built on Flask and SQLAlchemy, it structures role-based access control (Admin vs User), manages database relations (ParkingLot ➔ ParkingSpot ➔ Reservation), and integrates Chart.js to display occupancy analytics, automating parking spot management.

##### Problem Solved
* **Preventing Concurrent Double Booking**: Under high traffic, two users could click to book the same spot simultaneously, leading to double-booking database errors. The database model solves this by wrapping reservation updates in a transaction-safe state transition: it verifies the spot is in the 'A' (Available) state and updates it to 'O' (Occupied) as a single database transaction, rejecting overlapping requests.

##### Core Features
* **Relational Database Design**: Employs SQLAlchemy to map parking lots, spots, and reservations, implementing cascade deletion rules.
* **Role-Based Access Control**: Separates views for Admins (manage lots/spots, view users, set pricing) and Users (view spots, book/release spots).
* **Interactive Chart.js Dashboard**: Renders real-time statistics of occupancy and revenue for administrator audits.
* **Double-Booking Prevention**: Enforces transaction-level checks to prevent double-booking of parking spots.

##### Key Highlights
* **Real-time Occupancy Sensors**: Connect IoT sensors to automatically update spot states.
* **Dynamic Pricing Engine**: Implement algorithms that adjust hourly prices based on current occupancy.
* **GPS Navigation Integration**: Integrate map APIs to navigate users to their booked spots.

<br/>


#### Portfolio Portal - Personal Professional Index

**Elevator Pitch:** *Most developer portfolios are static HTML files that are difficult to update and lack dynamic content structures.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./MY PORTFOLIO ONLINE`

##### Overview
Most developer portfolios are static HTML files that are difficult to update and lack dynamic content structures. `Portfolio Portal` provides a dynamic, database-driven professional dashboard. Built with React, TypeScript, and Vite, it fetches project listings, academic milestones, and experience records from a Supabase PostgreSQL backend, displaying developer credentials dynamically.

##### Problem Solved
Addressed technical challenges in developing robust systems for MY PORTFOLIO ONLINE.

##### Core Features
* **Supabase Integration**: Connects with Supabase database clients to query dynamic project records.
* **Strict Type Safety**: Employs TypeScript across component interfaces, data structures, and database entities.
* **Modular Tailwind Design**: Uses TailwindCSS for fluid layouts and consistent UI scaling.

##### Key Highlights
* **Interactive Project Demos**: Embed live project simulators within card components.
* **Analytics Tracker**: Log page visits and popular project views using Supabase edge functions.

<br/>


#### QuantumPhaseEstimator - Qiskit Quantum Simulator

**Elevator Pitch:** *Simulating quantum algorithms on classical hardware is critical to verifying circuit gates before running them on expensive quantum processors.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python

**Repository Path:** `./quantum codes`

##### Overview
Simulating quantum algorithms on classical hardware is critical to verifying circuit gates before running them on expensive quantum processors. `QuantumPhaseEstimator` implements a phase estimation simulation. Built in Python using Qiskit and AerSimulator, it constructs quantum circuits, prepares counting and state qubits, applies the inverse Quantum Fourier Transform (QFT), and runs measurements, validating quantum algorithm mechanics.

##### Problem Solved
* **Qubit Ordering in IQFT Swap Gates**: Qiskit index mapping is little-endian, which reverses qubit order during measurements. The simulation solves this by implementing custom swap gates in the inverse QFT function, matching classical math specifications and preventing incorrect measurements.

##### Core Features
* **Inverse QFT Implementation**: Implements the inverse Quantum Fourier Transform using swap gates, Hadamard gates, and controlled phase rotations.
* **Eigenstate Preparation**: Prepares data qubits in specific states (e.g. |1> for T gates) to test phase measurements.
* **Qiskit Circuit Builder**: Configures quantum circuits with counting qubits, data qubits, and classical measurement registers.
* **AerSimulator Aer Runner**: Compiles and simulates circuits on local CPU simulators, extracting measurement statistics.

##### Key Highlights
* **Shor's Algorithm Integration**: Expand the IQFT module to simulate modular exponentiation for Shor's factoring.
* **Quantum Noise Simulation**: Add noise profiles to the AerSimulator to simulate physical quantum hardware environments.

<br/>


#### R&D Sandbox - Experimental Engineering Workspace

**Elevator Pitch:** *This folder serves as an isolated developer environment for testing new libraries, benchmarking algorithms, and drafting prototype features before integrating them into main project repositories.*

**Portfolio Tags:** `Beginner/Prototype` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./New folder`

##### Overview
This folder serves as an isolated developer environment for testing new libraries, benchmarking algorithms, and drafting prototype features before integrating them into main project repositories.

##### Problem Solved
Addressed technical challenges in developing robust systems for New folder.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### ResearchWorkspace - Master Project Portfolio

**Elevator Pitch:** *This folder is a master research workspace containing copy setups of active portfolio codebases (e.g.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Docker, Python, Jupyter Notebook, HTML, JavaScript, Node.js, CSS, TypeScript

**Repository Path:** `./projects`

##### Overview
This folder is a master research workspace containing copy setups of active portfolio codebases (e.g. Chatbots, COVID-19 ETL pipelines, and NLP classifiers). It serves as a central index and developer playground for systems testing.

##### Problem Solved
Addressed technical challenges in developing robust systems for projects.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### SIH Portal - Smart Matchmaking Internship Platform

**Elevator Pitch:** *University internship drives often suffer from manual resume screening, inefficient communication between companies and applicants, and fragmented tracking.*

**Portfolio Tags:** `Intermediate` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./SIH`

##### Overview
University internship drives often suffer from manual resume screening, inefficient communication between companies and applicants, and fragmented tracking. `SIH Portal` introduces a role-based, matching platform. Built with React and TypeScript, it implements workspaces for Students (tracking applications and matching scores), Companies (publishing templates and review queues), and Admins (auditing drives), providing a structured frontend portal for academic internship coordination.

##### Problem Solved
Addressed technical challenges in developing robust systems for SIH.

##### Core Features
* **Role-Based Workspace Isolation**: Configures distinct UI workflows and component subtrees for Students, Companies, and Administrators.
* **Dynamic Matching Layouts**: Tracks student eligibility percentages against published company requirements.
* **Polished Verification Queue**: Built-in admin panels to approve pending drives and review participant credentials.
* **Strict Type Safety**: Outlines interfaces for applications, user profiles, and internship templates in TypeScript.

##### Key Highlights
The platform is designed to handle high-frequency dashboard interactions. Rather than relying on simple state variables, it implements structured UI component subtrees (e.g. StudentDashboard, CompanyDashboard, AdminDashboard) linked to state filters, ensuring fast navigation and data updates.

<br/>


#### Second Brain - AI-Powered Personal Knowledge Graph

**Elevator Pitch:** *Engineers and researchers face high cognitive overhead when organizing disparate technical thoughts, articles, and journal entries.*

**Portfolio Tags:** `Advanced` | `Research` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./2nd brain`

##### Overview
Engineers and researchers face high cognitive overhead when organizing disparate technical thoughts, articles, and journal entries. Existing note-taking tools are static, lacking semantic relationships and contextual search. `Second Brain` introduces an automated, AI-driven tagging and indexing layer over note entries. By extracting important terms, calculating emotional sentiment indices, and generating automated summaries, the system transforms flat text entries into structured, queryable knowledge graphs synced to a cloud backend.

##### Problem Solved
* **State Sync and Local Transitions**: Managing reactive editing states while database writes are active can create jarring page reflows. The client implements optimistic UI updates, rendering notes instantly while transaction responses resolve in the background.

##### Core Features
* **Automated Metadata Extraction Pipeline**: Parses raw text entries to calculate sentiment metrics, generate tags, and isolate critical terminologies.
* **Supabase Client Layer**: Integrates client-side JWT authentication with relational schema mappings in Supabase.
* **Dynamic AI Chat Interface**: Features an interactive RAG-like playground where users query their aggregated notes through natural language conversations.
* **Polished State Syncing**: Orchestrates component states across dashboard filters, editing dialog states, and real-time database updates.

##### Key Highlights
`Second Brain` is engineered beyond simple database storage. It maps out a custom schema (`diary_entries`) containing array fields for `important_terms` and `tags` beside float fields for `sentiment` scores. When a user logs a note, the system treats it as a node in a personal knowledge graph. The frontend is built with modular state isolation (React + TypeScript), allowing immediate UI updates while background synchronization tasks write back to Supabase.

<br/>


#### SolarDiary - AI-Driven Gamified Journaling Engine

**Elevator Pitch:** *Students struggle to track their academic progress, milestones, and emotional health across dense schedules.*

**Portfolio Tags:** `Advanced` | `Research` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python

**Repository Path:** `./jarvis`

##### Overview
Students struggle to track their academic progress, milestones, and emotional health across dense schedules. Traditional organizers are static lists that fail to provide insight into behavioral patterns. `SolarDiary` introduces an AI-driven journaling and logging system. Built in Python, it parses academic events (exams, study sessions, achievements) using structured schemas, calculates progress metrics, maps entries to emotional tones (e.g. motivated, frustrated, proud), and runs a gamified point-allocation algorithm to track academic engagement over time.

##### Problem Solved
Addressed technical challenges in developing robust systems for jarvis.

##### Core Features
* **Abstract Log Parsing Engine**: Deploys object-oriented architecture (`diary_system.py`) to parse diverse event payloads (study durations, exam scores) into standard diary formats.
* **Behavioral Metric Calculators**: Evaluates data inputs to categorize sessions into specific emotional states and priority tiers.
* **Gamified Point Allocation**: Implements a rules-based scoring algorithm that awards progress points based on study achievements and task completions.
* **Relational JSON Exporter**: Exports session metrics to standardized JSON schemas, enabling easy integration with external databases.

##### Key Highlights
`SolarDiary` is built on strict OOP principles, using custom Enumerations (`DiaryEntryType`, `EmotionalTone`, `PriorityLevel`) and Dataclasses to guarantee data integrity. Instead of simple text files, it treats every daily log as a structured node, tracking study times, milestones, and emotional outcomes to create a clean timeline for behavioral analytics.

<br/>


#### SoulEcho - Persona Roleplay AI Platform

**Elevator Pitch:** *Standard LLMs reply with a generic, helpful tone that breaks immersion during creative writing or character roleplay.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, C/C++, HTML, JavaScript, Node.js, CSS

**Repository Path:** `./soul echo`

##### Overview
Standard LLMs reply with a generic, helpful tone that breaks immersion during creative writing or character roleplay. `SoulEcho` introduces a persona-tuned conversational platform. It manages user authentication, chat channels, and message histories using an Express.js backend and SQLite database. Dynamically, it routes prompts through python wrappers to the Groq SDK, applying strict prompt constraints (system profiles, dialogue context, and behavior rules) to load stable, immersive AI characters (e.g. Jungkook, Jimin), preventing model drift.

##### Problem Solved
* **Character Conversational Drift**: Standard LLM APIs default to a helpful assistant persona after several messages, forgetting their roleplay constraints. The system solves this by appending the character's system prompt (the behavior profile) before the chat history on *every* request, enforcing character constraints throughout the session.

##### Core Features
* **Python Persona Wrappers**: Employs Python wrapper scripts configuring Groq SDK hyper-parameters (temperature, top-p) to enforce distinct characters.
* **Context-Safe Prompt Templates**: Structures relational system prompts containing background contexts, speech styles, and relationship definitions.
* **Relational Message Logging**: Uses SQLite database schemas to log dialogue histories, maintaining persistent context across sessions.
* **JWT Express API Gateway**: Secures user channels and coordinates character selection routes.

##### Key Highlights
`SoulEcho` separates prompt configurations (`lovedone.py`, `jimin.py`) from the core Express API router, allowing developers to upload new characters without server restarts. It aggregates database logs to construct a rolling history window on every message request, passing previous interactions to the LLM to preserve roleplay continuity, avoiding memory constraints.

<br/>


#### SpaceX Launch Failure Capstone

**Elevator Pitch:** *Evaluating rocket landing success rates requires analyzing telemetry parameters, payload weights, orbit types, and launch sites.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, Jupyter Notebook

**Repository Path:** `./spacex failures systematic analysis`

##### Overview
Evaluating rocket landing success rates requires analyzing telemetry parameters, payload weights, orbit types, and launch sites. Manual compilation is error-prone and time-consuming. This Capstone project implements an end-to-end data science workflow. It scrapes launch tables from Wikipedia, runs SQL analyses, plots coordinates on interactive Folium maps, builds a Plotly Dash dashboard to visualize outcomes, and trains machine learning classifiers (Logistic Regression, SVM, Decision Trees, KNN) to predict landing success, illustrating a complete data pipeline.

##### Problem Solved
* **Inconsistent Wiki Tables Parsing**: Wikipedia tables change formats across historical years, leading to column misalignment during scraping. The scraper solves this by dynamically validating headers, mapping table cells based on keyword keys rather than fixed indexes, preventing data loss.

##### Core Features
* **Wikipedia Launch Table Scraper**: Uses BeautifulSoup and request libraries to parse HTML tables, extracting launch coordinates and payloads.
* **SQL Exploratory Data Analysis**: Ingests dataset tables into SQLite databases, running queries to analyze launch statistics.
* **Folium Interactive Maps**: Generates geospatial maps with coordinate markers and circle overlays indicating landing zones.
* **Plotly Dash Analytics Portal**: Builds a Python dashboard server rendering real-time scatter plots and dropdown filters.
* **ML Classifier Grid**: Trains and compares classifiers (SVM, KNN, Decision Trees), plotting confusion matrices.

##### Key Highlights
* **Real-time Launch Ingestion**: Connect the pipeline to Spacex API to automatically ingest new launch telemetry.
* **Distributed Model Serving**: Wrap the classification models in a FastAPI service.

<br/>


#### SpeechSTT - Speech-to-Text reference Guides

**Elevator Pitch:** *An isolated reference repository detailing speech recognition architectures, microphone capturing setups, and audio transcription engines.*

**Portfolio Tags:** `Beginner/Prototype` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./speech recognisation`

##### Overview
An isolated reference repository detailing speech recognition architectures, microphone capturing setups, and audio transcription engines.

##### Problem Solved
Addressed technical challenges in developing robust systems for speech recognisation.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### SreePort - Interactive Visual Portfolio

**Elevator Pitch:** *Standard web portfolios use static grids that fail to show the developer's creative styling skills.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, CSS, Python, JavaScript

**Repository Path:** `./portfolio website`

##### Overview
Standard web portfolios use static grids that fail to show the developer's creative styling skills. `SreePort` provides an interactive professional portfolio website for "O. Sree Chakra Reddy". Built with Tailwind CSS, GSAP, and custom VFX modules (`vfx.js` with text-shuffling animations), it structures dedicated project pages for complex engineering builds, detailing machine learning pipelines, quantum circuits, and systems architectures.

##### Problem Solved
Addressed technical challenges in developing robust systems for portfolio website.

##### Core Features
* **GSAP Animation System**: Deploys GreenSock timelines to orchestrate entrance animations, text shuffles, and smooth layout reflows.
* **Tailwind Dark Mode UI**: Built on utility-first Tailwind CSS classes with integrated dark theme structures.
* **Creative Visual Effects**: Features canvas shaders and text-shuffling scripts (`vfx.js`) that animate on user interactions.
* **Modular Page Templates**: Implements structured project profiles (e.g. churn predictions, credit scoring, deepfake classification).

##### Key Highlights
* **Dynamic Markdown Parsing**: Integrate client-side Markdown parsers to load project detail files dynamically.
* **Three.js WebGL background**: Build interactive 3D particle grids that respond to cursor movements.

<br/>


#### Student CV Web Portal - Semantic HTML Portfolio

**Elevator Pitch:** *Static resume files are difficult to search and lack direct links to developer profiles.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML

**Repository Path:** `./html`

##### Overview
Static resume files are difficult to search and lack direct links to developer profiles. `Student CV Web Portal` provides an online academic resume. Built using semantic HTML5, it organizes directories into dedicated pages (Home, Academics, Personal, Resume, Contact), structuring tables to present academic transcripts and credentials.

##### Problem Solved
Addressed technical challenges in developing robust systems for html.

##### Core Features
* **Semantic Document Hierarchy**: Uses HTML5 tags (`address`, `table`, `form`) to structure document layouts.
* **Multi-Page Route Map**: Implements local navigation paths to link resume sub-sections.
* **Data Presentation Tables**: Structures tables to display subject lists and grades.

##### Key Highlights
* **TailwindCSS Integration**: Style layout files using a utility-first CSS framework.
* **Dynamic Contact Form**: Add a backend endpoint to handle contact form submissions.

<br/>


#### SystemsConfig - Hardware Configurations

**Elevator Pitch:** *This repository contains reference configurations and parameters for hardware integrations, micro-controller operations, and interface setups.*

**Portfolio Tags:** `Beginner/Prototype` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./intenal mpmc`

##### Overview
This repository contains reference configurations and parameters for hardware integrations, micro-controller operations, and interface setups.

##### Problem Solved
Addressed technical challenges in developing robust systems for intenal mpmc.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### T7 MediScan AI - Backend

**Elevator Pitch:** *================================== A guide to masked arrays in NumPy ==================================*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, C/C++, HTML, JavaScript, Node.js, CSS

**Repository Path:** `./hackathon t7 cardano`

##### Overview
==================================
A guide to masked arrays in NumPy
==================================

##### Problem Solved
Addressed technical challenges in developing robust systems for hackathon t7 cardano.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### TaxiFarePredictor - Tabular ML forecasting Pipeline

**Elevator Pitch:** *Predicting urban transit pricing requires modeling complex spatio-temporal dependencies, weather indicators, and historical passenger demands.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Jupyter Notebook

**Repository Path:** `./IIT M PROJECTS`

##### Overview
Predicting urban transit pricing requires modeling complex spatio-temporal dependencies, weather indicators, and historical passenger demands. Linear models fail to capture non-linear traffic hotspots and peak-hour multipliers. `TaxiFarePredictor` establishes a structured machine learning pipeline that ingests raw tabular transit records, engineers spatial features (haversine distances, coordinates clustering), and trains optimized gradient boosting models (XGBoost, RandomForest) to forecast travel costs, targeting Kaggle-level performance.

##### Problem Solved
* **Memory Limits on Large Datasets**: Tabular datasets with millions of rows quickly fill up system memory. The pipeline addresses this by optimizing DataFrame schema typing (replacing float64 with float32 and casting category fields), reducing memory usage by over 60% during model training.

##### Core Features
* **Advanced Feature Engineering**: Computes Haversine distance vectors, directional bearings, and coordinate bin clusters from raw latitude/longitude points.
* **DateTime Deconstruction**: Deconstructs timestamps into cyclically encoded parameters (hour of day, day of week, month) to capture temporal traffic patterns.
* **Gradient Boosting Regressors**: Integrates tree-based regression models (XGBoost, LightGBM) to handle high-cardinality data fields.
* **Automated Parameter Tuning**: Employs GridSearchCV workflows to optimize learning rates, maximum tree depths, and estimator weights.

##### Key Highlights
`TaxiFarePredictor` addresses outlier filtering and coordinate validation directly in the preprocessing layer. It handles bad sensor inputs (coordinates outside geographical bounds) and computes direct geodesic distances. The feature selection pipeline scales to millions of rows, avoiding memory overflows by converting feature datatypes to compact formats (e.g. float32, int8).

<br/>


#### Team7 Slides - Farm Rental Pitch Deck

**Elevator Pitch:** *This folder contains the business proposals and slides for the Agri-Rental platform proposed by Team 7, detailing market opportunities and platform concepts.*

**Portfolio Tags:** `Beginner/Prototype` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** General Programming

**Repository Path:** `./team 7`

##### Overview
This folder contains the business proposals and slides for the Agri-Rental platform proposed by Team 7, detailing market opportunities and platform concepts.

##### Problem Solved
Addressed technical challenges in developing robust systems for team 7.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### TitanicPredictor - Kaggle Machine Learning Pipeline

**Elevator Pitch:** *Tabular datasets from public challenges are often noisy and contain missing fields, making model training unstable.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./titanic classification`

##### Overview
Tabular datasets from public challenges are often noisy and contain missing fields, making model training unstable. `TitanicPredictor` implements an end-to-end classification pipeline. It loads demographic records, imputes missing values (age, embarked), encodes categories, scales features, and evaluates classifiers (Logistic Regression, Random Forest, XGBoost) using cross-validation, predicting passenger survival.

##### Problem Solved
Addressed technical challenges in developing robust systems for titanic classification.

##### Core Features
* **Feature Engineering Pipeline**: Imputes missing fields, one-hot encodes category features, and standardizes numeric columns.
* **Model Grid Search**: Optimizes hyperparameters (n_estimators, max_depth) using cross-validation loops.
* **Metrics Comparison**: Compares classifiers using confusion matrices, precision-recall, and ROC-AUC curves.

##### Key Highlights
* **Deep Tabular Models**: Implement PyTorch TabNet to benchmark deep learning models against gradient boosted trees.
* **API Service**: Deploy the model to an API endpoint using FastAPI.

<br/>


#### Trekking Management Application

**Elevator Pitch:** *This is a basic Flask web application for managing trekking events.*

**Portfolio Tags:** `Intermediate` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, Python

**Repository Path:** `./mad 1 project`

##### Overview
This is a basic Flask web application for managing trekking events. It is made in a simple beginner-friendly style using Flask, Jinja templates, Bootstrap, and SQLite.

##### Problem Solved
Addressed technical challenges in developing robust systems for mad 1 project.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### UMAX Fitness AI - Kinetic Motion Analyzer

**Elevator Pitch:** *Analyzing athletic movements (e.g.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./UMAX FITNESS APP`

##### Overview
Analyzing athletic movements (e.g. punch speed, kick force) manually is difficult without expensive bio-mechanical sensors. `UMAX Fitness AI` introduces a web-based bio-mechanical tracker. Built in Python, it captures live camera streams, extracts skeletal coordinates using MediaPipe Pose and Hands, and applies kinematics equations to estimate strike speed and force outputs in real time, converting standard webcams into motion analysis tools.

##### Problem Solved
* **Voice Feedback Delay**: Synchronous speech synthesis blocks the computer vision loop, causing frame drops. The assistant solves this by running text-to-speech tasks in a separate background thread, passing commands through a thread-safe queue, keeping the camera capture loop running at a steady 30 FPS.

##### Core Features
* **MediaPipe Landmark Tracking**: Extracts spatial coordinates for limbs, hands, and joints at high frame rates.
* **Kinetic Force calculations**: Estimates physical impulse-force (in Newtons) using kinematics equations based on estimated limb mass and strike deceleration.
* **Fist State Geometry**: Evaluates distance ratios between fingers and wrist landmarks to verify a closed fist before logging punches.
* **State Machine Strike Detector**: Implements a state machine (`IDLE`, `ACCELERATING`, `DECELERATING`, `COOLDOWN`) to accurately count strikes.
* **Multi-threaded Speech Integration**: Links background threads using Pyttsx3 and SpeechRecognition, allowing hands-free voice control.
* **PyAutoGUI Keystroke Mappings**: Converts physical punches to keyboard inputs, enabling gesture control.

##### Key Highlights
`UMAX Fitness AI` integrates raw physics calculations with computer vision tracking. Instead of just counting movements, it estimates the physical force output of each strike. The state machine filters out noise and jitter, ensuring that only clean, high-velocity movements register as strikes.

<br/>


#### VisionAgent - Real-Time Browser-Based AI Vision System

**Elevator Pitch:** *Building real-time computer vision applications in the browser often introduces massive latency due to raw frame sizes and slow API serialization.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./CV INTEGRATED BOT`

##### Overview
Building real-time computer vision applications in the browser often introduces massive latency due to raw frame sizes and slow API serialization. `VisionAgent` establishes a lightweight, local-first capture architecture. It interfaces with the client's webcam using HTML5 canvas streams, packages frames efficiently, and exposes them to cloud-hosted vision-language models (like LLaVA or Claude Vision via Groq/API endpoints). This framework provides a scalable foundation for client-side visual telemetry and real-time object classification.

##### Problem Solved
* **UI Thread Lag and Frame Drops**: Sending continuous camera feeds to cloud APIs can freeze browser render threads. The capture pipeline solves this by decoupling webcam loops from API dispatches, sampling frames at a structured throttle rate (e.g. 1 frame/sec) and drawing frames onto a virtual canvas, maintaining a smooth 60 FPS client UI.

##### Core Features
* **Low-Latency Camera Hook**: Implements a React hook (`useCamera`) that hooks into browser media streams, rendering to canvas with optimized frame intervals.
* **Vision Service API**: Configures a service wrapper (`visionService`) that serializes frame data and pipelines it to vision model APIs.
* **Real-Time Telemetry Panels**: Features a results renderer (`ResultsPanel`) displaying model predictions, token metrics, and execution latency.
* **Strict Type Safety**: Outlines data contracts (`types/vision.ts`) defining video feeds, inference responses, and bounding box states.

##### Key Highlights
`VisionAgent` is designed to run completely asynchronously. The client-side hook captures camera inputs without blocking the main browser thread, and frames are dispatched in a non-blocking queue. The codebase is pre-configured with modular services, allowing developer-level configuration of models, API keys, and frame capture rates.

<br/>


#### VisionOS-Agent - Desktop Automation Runtime Environment

**Elevator Pitch:** *Traditional robotic process automation (RPA) systems rely on fragile, coordinate-based scripts that break whenever screen resolutions or UI layouts shift.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./SCREEN AUTOMATION`

##### Overview
Traditional robotic process automation (RPA) systems rely on fragile, coordinate-based scripts that break whenever screen resolutions or UI layouts shift. `VisionOS-Agent` establishes a robust, vision-guided computer control framework. It captures live desktop screen states, runs high-fidelity optical character recognition (OCR) via Tesseract, parses screen elements, and dispatches real-time screenshot structures to LLMs (via Groq API). By executing structured JSON action scripts (mouse movements, clicks, keystrokes, clipboard actions) on the native OS, it enables resilient, cognitive desktop automation.

##### Problem Solved
* **Dynamic Resolution and Layout Shifts**: Coordinate-based clicking fails when windows are resized or layouts change. The agent resolves this by running local OCR: it scans the screen for the target text label (e.g. "Submit"), calculates the bounding box midpoint, and moves the mouse directly to that spatial location, maintaining layout-agnostic execution.

##### Core Features
* **OCR-Guided Interactive Anchor Detection**: Employs Tesseract OCR and PIL image processing to locate textual buttons and UI inputs on screen, avoiding coordinate dependency.
* **Non-Blocking Execution Loop**: Orchestrates asynchronous tasks and UI capture loops without freezing, utilizing Python multi-threading.
* **Dynamic Action Dispatcher**: Parses structured JSON response payloads into safe, localized system calls (`pyautogui`).
* **Emergency Fail-Safe Protocols**: Configures mouse-corner failsafes (`FAILSAFE = True`) and precise execution delays to prevent runaway interface loops.

##### Key Highlights
`VisionOS-Agent` does not just blindly type keystrokes. It coordinates visual feedback (screenshots + OCR) with LLM prompt history to verify actions. The agent reads clipboard text, tracks active window handles (`winreg` & `win32gui`), and uses image analysis to confirm the success of each action before executing the next instruction in its queue, matching enterprise-level robustness.

<br/>


#### VoiceAssistant & Webhook - AI Desktop Companion

**Elevator Pitch:** *Traditional virtual assistants lack custom API integrations or conversational flexibility.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./python`

##### Overview
Traditional virtual assistants lack custom API integrations or conversational flexibility. `VoiceAssistant` provides an AI-powered desktop companion and Messenger integration. Built in Python using Flask, it captures microphone inputs, processes audio using Google Speech-to-Text, runs conversational prompts via OpenAI APIs, and speaks back responses via Google Text-to-Speech (gTTS), bridging conversational models with local systems.

##### Problem Solved
* **Messenger Webhook Verification**: Facebook webhooks require strict token validation before activation. The Flask app implements a verification route that audits tokens (`VERIFY_TOKEN`) and replies with validation states, enabling instant webhook setup.

##### Core Features
* **Dual Interface Gateways**: Outlines a desktop microphone loop and a Facebook Messenger webhook Flask API.
* **Offline Audio Capturing**: Integrates PyAudio and SpeechRecognition to record and parse microphone inputs.
* **Google TTS Synthesizer**: Converts model outputs into spoken audio files.
* **JSON Webhook Controller**: Parses incoming messenger payloads and routes responses.

##### Key Highlights
* **Local TTS/STT Engine**: Migrate to local models (e.g. Whisper and Piper) to run offline.
* **Smart Home Integrations**: Map voice commands to trigger IoT actions (e.g. smart lights).

<br/>


#### VoiceCircleAI - Multimodal Voice Assistant

**Elevator Pitch:** *Deploying voice assistants introduces challenges including slow TTS response times, duplicate API query costs, and complex local development setups.*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Node.js, HTML, JavaScript, Docker

**Repository Path:** `./voice-circle-ai`

##### Overview
Deploying voice assistants introduces challenges including slow TTS response times, duplicate API query costs, and complex local development setups. `VoiceCircleAI` provides a containerized multimodal voice assistant. It features an animated circle UI that shifts states (`listening`, `processing`, `speaking`), routes calls through an Express backend proxying Groq APIs, implements a Time-To-Live (TTL) cache to save API usage costs, and containerizes services using Docker Compose, delivering a production-ready assistant.

##### Problem Solved
* **Inference Delay and API Cost Overhead**: Frequent voice requests cause response lag and inflate cloud API bills. The system solves this by implementing an in-memory cache with TTL (5-minute expiration) on the backend, serving repeat queries instantly from memory and reducing API requests by up to 40%.

##### Core Features
* **State-Aware Canvas UI**: Implements a responsive React circle avatar that shifts colors, dimensions, and animations dynamically.
* **In-Memory TTL Cache**: Features backend caching with Time-To-Live (TTL) parameters to store recent queries, minimizing duplicate API requests.
* **Express API Gateway**: Proxies requests securely to Groq APIs (Llama, Mixtral, Gemma).
* **Operations Security**: Configures rate limiters, request loggers, and error handlers.
* **Multi-Container Docker Deployment**: Containerizes frontend, backend, and Nginx proxy servers using Docker Compose.

##### Key Highlights
* **Local TTS Engine Integration**: Replace browser TTS with local models (e.g. Piper) to improve voice quality.
* **Redis Cache Database**: Migrate in-memory caches to a Redis cluster to support distributed servers.
* **Observability Dashboard**: Build dashboard panels to track request rates, cache hits, and response times.

<br/>


#### VoiceOrchestrator - Multi-Agent Voice Automation Portal

**Elevator Pitch:** *Standard voice interfaces (like Alexa or Siri) run on closed ecosystems that are difficult to customize or integrate into custom web developer environments.*

**Portfolio Tags:** `Advanced` | `Prototype` | `Artificial Intelligence & Machine Learning`

**Technologies:** Node.js, HTML, JavaScript

**Repository Path:** `./voice multi`

##### Overview
Standard voice interfaces (like Alexa or Siri) run on closed ecosystems that are difficult to customize or integrate into custom web developer environments. `VoiceOrchestrator` provides an interactive voice command console. It captures microphone inputs via the browser Web Speech API, routes transcriptions to Groq models (Express backend) to translate spoken phrases into structured JSON automation scripts, and executes actions on the React frontend dashboard, enabling hands-free web control.

##### Problem Solved
* **LLM Syntax Anomalies in JSON Parsing**: Generative models frequently output extra markdown blocks (e.g. ```json ... ```) that crash JSON parsing functions. The parser solves this by using regex sanitizers to strip markdown blocks and extract raw JSON strings before processing, preventing script failures.

##### Core Features
* **Web Speech API STT/TTS**: Captures browser-native audio streams and translates them to text, returning voice responses.
* **JSON Action Spec Parser**: Translates LLM completions into structured JSON automation scripts (e.g. navigation, scrolling, clicking).
* **Visual Log Panel**: Implements an interactive execution feed rendering inputs, JSON scripts, and model outputs.
* **Express API proxy**: Interfaces securely with the Groq API, protecting API keys.

##### Key Highlights
* **Local Whisper Server**: Migrate to local Whisper servers to run offline speech recognition.
* **Browser Extension**: Pack the automation engine into a Chrome extension to control any website.

<br/>


#### WikiChat Gateway - Context-Aware NLP Agent

**Elevator Pitch:** *Modern LLMs and conversational agents face significant information latency, rendering them incapable of answering queries about real-time, evolving world events without high retrieval costs.*

**Portfolio Tags:** `Advanced` | `Completed` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python

**Repository Path:** `./1`

##### Overview
Modern LLMs and conversational agents face significant information latency, rendering them incapable of answering queries about real-time, evolving world events without high retrieval costs. `WikiChat Gateway` solves this by introducing a lightweight, state-preserving conversational routing controller that intercepts user intents and dynamically maps them to live external knowledge repositories (like Wikipedia's API). This architecture allows low-latency, real-world factual retrieval without training overhead, serving as a lightweight alternative to full-scale semantic search architectures.

##### Problem Solved
* **Search Ambiguity & API Failures**: Standard API calls for specific search queries frequently fail due to spelling variations or ambiguous matching. The pipeline implements a recursive fallback queue: if the direct summary fails, it triggers a candidate list search, running secondary API checks until a valid payload is retrieved, eliminating client-side empty responses.

##### Core Features
* **Dynamic Intent-Registration Hooks**: Employs a custom `@register_call` decorator pattern that maps specific input queries (e.g., "whoIs") to dedicated callback handlers.
* **API Disambiguation Resolver**: Implements a self-healing Wikipedia search loop that automatically falls back to secondary candidates if the primary query fails, optimizing retrieval success rate.
* **State-Preserving Conversational Flow**: Integrates template-based chat state orchestration, ensuring the session memory is maintained across conversational exchanges.

##### Key Highlights
Most conversational bots rely on static rule files or heavy RAG setups that introduce high computation costs. `WikiChat Gateway` uses an event-driven hook system to bind API lookups directly to pattern registrations. This hybrid approach enables execution-level modularity where new knowledge tools can be registered dynamically in a single line of code, turning a standard prompt loop into an extensible agent gateway.

<br/>


#### parsing/tests/test_autolev.py uses the .al files in this directory as inputs and checks

**Elevator Pitch:** *Font Metrics for the 14 PDF Core Fonts ======================================*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, C/C++, HTML, JavaScript, Node.js, CSS

**Repository Path:** `./cardano hackathon`

##### Overview
Font Metrics for the 14 PDF Core Fonts
======================================

##### Problem Solved
Addressed technical challenges in developing robust systems for cardano hackathon.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### parsing/tests/test_autolev.py uses the .al files in this directory as inputs and checks

**Elevator Pitch:** *Font Metrics for the 14 PDF Core Fonts ======================================*

**Portfolio Tags:** `Advanced` | `Production` | `Artificial Intelligence & Machine Learning`

**Technologies:** Python, C/C++, HTML, JavaScript, Node.js, CSS

**Repository Path:** `./new hackathon final if`

##### Overview
Font Metrics for the 14 PDF Core Fonts
======================================

##### Problem Solved
Addressed technical challenges in developing robust systems for new hackathon final if.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


### ??️ Data Science & Analytics
---

#### Jupyter Notebook

**Elevator Pitch:** *A project exploring jupyter notebook.*

**Portfolio Tags:** `Beginner/Prototype` | `Completed` | `Data Science & Analytics`

**Technologies:** Jupyter Notebook

**Repository Path:** `./jupyter notebook`

##### Overview
A project exploring jupyter notebook.

##### Problem Solved
Addressed technical challenges in developing robust systems for jupyter notebook.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### ProjectScanner - Automated Workspace Auditor

**Elevator Pitch:** *Managing a multi-project workspace manually makes it difficult to track file sizes, identify codebases, or generate portfolios.*

**Portfolio Tags:** `Intermediate` | `Completed` | `Data Science & Analytics`

**Technologies:** Python

**Repository Path:** `./portfolio_scripts`

##### Overview
Managing a multi-project workspace manually makes it difficult to track file sizes, identify codebases, or generate portfolios. `ProjectScanner` provides an automated workspace auditor. Written in Python, it walks directory structures, ignores virtual environments, hashes file listings to detect code changes, and exports a structured JSON report (`project_analysis.json`), enabling script-driven portfolio indexing.

##### Problem Solved
Addressed technical challenges in developing robust systems for portfolio_scripts.

##### Core Features
* **Recursive Directory Traversal**: Employs optimized `os.walk` loops with in-place directory pruning to bypass node modules and virtual environments.
* **State Change Hashing**: Computes MD5/SHA256 hashes of file structures to detect code updates.
* **Automated JSON Ingest**: Compiles file configurations and metadata into structured JSON indexes.

##### Key Highlights
* **CI/CD Integration**: Hook the script to GitHub Actions to automatically update portfolio indexes on git push events.
* **Interactive CLI Visualizer**: Build a CLI dashboard to print project summaries.

<br/>


### ??️ Research & Academic Projects
---

#### QuantumDocs - Systems Engineering Notes

**Elevator Pitch:** *This repository aggregates technical notes, documentation, and multiple integral study guides, serving as an academic reference library.*

**Portfolio Tags:** `Intermediate` | `Research` | `Research & Academic Projects`

**Technologies:** C/C++

**Repository Path:** `./quantum`

##### Overview
This repository aggregates technical notes, documentation, and multiple integral study guides, serving as an academic reference library.

##### Problem Solved
Addressed technical challenges in developing robust systems for quantum.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


### ??️ Software Engineering
---

#### Product R&D - Concept Sandboxes & Specifications

**Elevator Pitch:** *This repository serves as a workspace for drafting product specifications and design mockups, bridging the gap between product strategy and engineering execution.*

**Portfolio Tags:** `Beginner/Prototype` | `Prototype` | `Software Engineering`

**Technologies:** General Programming

**Repository Path:** `./PRODUCT`

##### Overview
This repository serves as a workspace for drafting product specifications and design mockups, bridging the gap between product strategy and engineering execution.

##### Problem Solved
Addressed technical challenges in developing robust systems for PRODUCT.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


### ??️ Web Development
---

#### DevSandbox - Script Benchmarks & Prototypes

**Elevator Pitch:** *An isolated directory dedicated to software prototyping, tracing development paths, testing third-party configurations, and benchmarking javascript execution loops.*

**Portfolio Tags:** `Beginner/Prototype` | `Prototype` | `Web Development`

**Technologies:** Node.js, HTML, JavaScript

**Repository Path:** `./incomplete`

##### Overview
An isolated directory dedicated to software prototyping, tracing development paths, testing third-party configurations, and benchmarking javascript execution loops.

##### Problem Solved
Addressed technical challenges in developing robust systems for incomplete.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### GlitchCanvas - Interactive Creative Portfolio

**Elevator Pitch:** *Standard developer portfolios lack visual impact and interactive elements.*

**Portfolio Tags:** `Intermediate` | `Production` | `Web Development`

**Technologies:** HTML, JavaScript, Node.js, TypeScript, CSS

**Repository Path:** `./my portfolio`

##### Overview
Standard developer portfolios lack visual impact and interactive elements. `GlitchCanvas` provides a high-impact creative dashboard. Built with React and Vite, it deploys custom canvas drawing loops (`LetterGlitch.jsx`) and CSS keyframe animations to render interactive glitch text overlays, delivering a modern, responsive landing page.

##### Problem Solved
Addressed technical challenges in developing robust systems for my portfolio.

##### Core Features
* **Interactive Canvas Loops**: Uses HTML5 Canvas APIs inside React structures to render random matrix characters.
* **Glitch Animation Shaders**: Implements CSS keyframe animations mapping RGB offsets on text states.
* **Fast Vite Bundler**: Configures Vite React plugins to generate low-overhead production bundles.

##### Key Highlights
* **WebGL Shaders**: Upgrade canvas loops to WebGL using Three.js to render complex visual effects.
* **Dynamic Project Feeds**: Connect the project grid to a Markdown file parser to automate updates.

<br/>


#### Personal Page - Static HTML Profile

**Elevator Pitch:** *A simple, static personal profile page structuring background image overlays and layout alignments, showcasing responsive web design.*

**Portfolio Tags:** `Beginner/Prototype` | `Completed` | `Web Development`

**Technologies:** HTML

**Repository Path:** `./my website`

##### Overview
A simple, static personal profile page structuring background image overlays and layout alignments, showcasing responsive web design.

##### Problem Solved
Addressed technical challenges in developing robust systems for my website.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


#### UILabs - Experimental Interface Playground

**Elevator Pitch:** *This repository serves as a frontend interface testing playground.*

**Portfolio Tags:** `Beginner/Prototype` | `Production` | `Web Development`

**Technologies:** Node.js, HTML, JavaScript

**Repository Path:** `./idk`

##### Overview
This repository serves as a frontend interface testing playground. It aggregates experimental HTML structures and vanilla JavaScript routines, providing an isolated environment to draft responsive design layouts, grid alignments, and canvas drawing tests before migrating code to production portals.

##### Problem Solved
Addressed technical challenges in developing robust systems for idk.

##### Core Features
- Implemented core system logic.
- Integrated modern technology stacks.
- Structured project for scalability.

##### Key Highlights
Demonstrates clean architecture and best practices.

<br/>


## ?? Portfolio Statistics
- **Total Projects:** 74
- **Total Technologies Used:** 12
- **Total Categories:** 5
- **Estimated Development Scope:** High-Volume Engineering & Research Repository
- **Strongest Domains:** Artificial Intelligence & Machine Learning, Web Development, Data Science & Analytics