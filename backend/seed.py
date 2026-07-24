from models import Project, SessionLocal, create_tables

PROJECTS = [
    {
        "title": "Homepedia",
        "slug": "homepedia",
        "category": "BIGDATA",
        "description": "French real-estate data platform aggregating DVF transactions, rental prices and socio-economic indicators across all communes.",
        "long_description": (
            "Homepedia is an Epitech T-DAT-902 group project building a full real-estate intelligence platform. "
            "My responsibility was the ProcessDataService: a PySpark ETL pipeline that ingests raw data from PostgreSQL "
            "(transactions_dvf, loyers_oll, indicateurs_communes) and MongoDB (sentiment scores), computes commune-level "
            "aggregates and pre-renders GeoJSON FeatureCollections into geo_cache_* tables consumed by the FastAPI backend. "
            "Key challenge: optimising a Spark job that was crashing due to shuffling 35 000 large PostGIS MultiPolygon "
            "strings — solved with ST_SimplifyPreserveTopology and geometry caching before the groupBy."
        ),
        "tech_stack": ["PySpark", "PostgreSQL", "PostGIS", "MongoDB", "FastAPI", "Mapbox GL", "Docker"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2025",
        "team_size": 4,
        "tags": ["ETL", "GeoJSON", "Real Estate", "Spark"],
        "order": 1,
    },
    {
        "title": "KubeQuest",
        "slug": "kubequest",
        "category": "DEVOPS",
        "description": "Production-grade Kubernetes cluster on AWS EC2 with full observability stack — Prometheus, Grafana and Loki.",
        "long_description": (
            "KubeQuest (Epitech T-CLO-902) deploys a multi-node Kubernetes cluster across 4 AWS EC2 t4g.medium instances "
            "in eu-west-3 (Paris). The cluster includes a control-plane + worker node, two additional workers, a dedicated "
            "ingress controller and a monitoring node running Prometheus, Grafana and Loki. "
            "The project covers kubeadm bootstrapping, CNI networking, ingress routing, persistent storage, "
            "and a fully automated observability pipeline with alerting rules."
        ),
        "tech_stack": ["Kubernetes", "AWS EC2", "Prometheus", "Grafana", "Loki", "kubeadm", "Helm"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2025",
        "team_size": 3,
        "tags": ["Cloud", "K8s", "Monitoring", "DevOps"],
        "order": 2,
    },
    {
        "title": "Visiobook",
        "slug": "visiobook",
        "category": "WEB",
        "description": "Microservices video-booking platform with Vue.js frontend, Node.js services and integrated Stripe payments.",
        "long_description": (
            "Visiobook is an Epitech group project building a video-consultation booking platform. "
            "The architecture uses three independent Node.js microservices — user, notification and payment — "
            "each with its own database and event communication. "
            "I worked on the core-payment-service integrating Stripe Checkout, webhooks for payment confirmation, "
            "and the Vue.js web-user-portal providing the booking flow, authentication and real-time notifications."
        ),
        "tech_stack": ["Vue.js", "Node.js", "Stripe", "PostgreSQL", "Docker", "REST API"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2024",
        "team_size": 4,
        "tags": ["Microservices", "Payments", "Vue", "Booking"],
        "order": 3,
    },
    {
        "title": "AFP News AI",
        "slug": "afp-news-ai",
        "category": "AI",
        "description": "NLP pipeline for French news classification using CamemBERT, spaCy NER, Neo4j knowledge graph and speech-to-text.",
        "long_description": (
            "A technical challenge built for AFP (Agence France-Presse) to automatically process and classify French news articles. "
            "The pipeline chains: speech-to-text transcription, spaCy named-entity recognition, "
            "CamemBERT fine-tuned for topic classification, and a Neo4j knowledge graph to surface entity relationships across articles. "
            "An orchestrator service coordinates the models via a REST API, all containerised with Docker Compose."
        ),
        "tech_stack": ["CamemBERT", "BERT", "spaCy", "Neo4j", "FastAPI", "Docker", "Python"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2025",
        "team_size": 1,
        "tags": ["NLP", "Knowledge Graph", "French NLP", "Classification"],
        "order": 4,
    },
    {
        "title": "Medical Imaging AI",
        "slug": "medical-imaging",
        "category": "AI",
        "description": "Deep learning classifier for medical images using DenseNet-121 and EfficientNetB0 with Grad-CAM visualisation.",
        "long_description": (
            "Epitech T-DEV-810 project applying deep learning to medical image classification. "
            "Compared DenseNet-121 and EfficientNetB0 architectures on a labelled medical dataset, "
            "implemented Grad-CAM to produce saliency maps that highlight the regions driving each prediction, "
            "and benchmarked both models with precision, recall and AUC metrics. "
            "Training ran on CUDA-accelerated hardware with mixed-precision to reduce memory footprint."
        ),
        "tech_stack": ["TensorFlow", "DenseNet-121", "EfficientNetB0", "Grad-CAM", "CUDA", "Python", "Matplotlib"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2024",
        "team_size": 2,
        "tags": ["Computer Vision", "Grad-CAM", "Healthcare", "Deep Learning"],
        "order": 5,
    },
    {
        "title": "MNIST Neural Network",
        "slug": "mnist-nn",
        "category": "AI",
        "description": "From-scratch CNN trained on MNIST with TensorFlow/Keras, including custom visualisation of training dynamics.",
        "long_description": (
            "A focused deep-learning project building, training and evaluating a Convolutional Neural Network on the MNIST "
            "handwritten-digit dataset using TensorFlow/Keras. "
            "Covers dataset exploration, model architecture design, training loop with callbacks, "
            "confusion-matrix analysis and custom matplotlib visualisations of loss curves and misclassified samples. "
            "Trained locally with CUDA 12.1 on WSL2."
        ),
        "tech_stack": ["TensorFlow", "Keras", "CUDA", "NumPy", "Matplotlib", "Seaborn", "Python"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2024",
        "team_size": 1,
        "tags": ["CNN", "Computer Vision", "CUDA", "Classification"],
        "order": 6,
    },
    {
        "title": "Slowwave",
        "slug": "slowwave",
        "category": "WEB",
        "description": "Full-stack music discovery web app built with Ruby on Rails during Le Wagon bootcamp.",
        "long_description": (
            "Slowwave is a music-discovery and sharing platform built as the final project of the Le Wagon coding bootcamp. "
            "It uses Ruby on Rails with a PostgreSQL database, Stimulus.js for progressive interactivity, "
            "and a custom CSS design system. Features include user authentication (Devise), "
            "playlist creation, track search integration and responsive layout."
        ),
        "tech_stack": ["Ruby on Rails", "PostgreSQL", "Stimulus.js", "Heroku", "Bootstrap", "JavaScript"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2023",
        "team_size": 4,
        "tags": ["Rails", "Le Wagon", "Music", "Full Stack"],
        "order": 7,
    },
    {
        "title": "Liquor Sales Big Data",
        "slug": "liquor-sales",
        "category": "BIGDATA",
        "description": "Large-scale analysis of Iowa liquor sales dataset using distributed computing and interactive dashboards.",
        "long_description": (
            "Epitech T-DAT-901 project performing exploratory and predictive analysis on the Iowa Liquor Sales public dataset "
            "(millions of records). The pipeline uses PySpark for distributed aggregations, "
            "identifies top-selling categories and seasonal trends, and exposes results through interactive Plotly dashboards. "
            "Includes a machine-learning component forecasting monthly sales by county."
        ),
        "tech_stack": ["PySpark", "Pandas", "Plotly", "Scikit-learn", "Python", "Jupyter"],
        "thumbnail": "",
        "video_url": "",
        "github_url": "https://github.com/camilogzlez",
        "demo_url": "",
        "year": "2024",
        "team_size": 2,
        "tags": ["EDA", "Forecasting", "Distributed", "Dashboards"],
        "order": 8,
    },
]


def seed():
    create_tables()
    db = SessionLocal()
    if db.query(Project).count() > 0:
        print("Database already seeded — skipping.")
        db.close()
        return
    for data in PROJECTS:
        db.add(Project(**data))
    db.commit()
    db.close()
    print(f"Seeded {len(PROJECTS)} projects.")


if __name__ == "__main__":
    seed()
