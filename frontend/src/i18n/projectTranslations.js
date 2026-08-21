// French overrides for project description / long_description, keyed by
// slug. Titles, category labels, and project-type badges stay in English
// in both locales by design -- only the prose descriptions are translated.
// Falls back to the API's (English) text when a slug has no entry here.
export const projectTranslationsFr = {
  homepedia: {
    description:
      "Plateforme d'analyse du marché immobilier ingérant plus de 822K transactions immobilières françaises, avec requêtes géospatiales, analyse de sentiment NLP sur les avis de villes, et historique de prix sur 12 mois.",
    long_description:
      "HomePedia est une plateforme d'intelligence immobilière full-stack conçue pour le marché français. Elle agrège des millions d'enregistrements issus de jeux de données publics ouverts — transactions immobilières DVF, diagnostics énergétiques DPE, données démographiques INSEE, enquêtes locatives ANIL, points d'intérêt OpenStreetMap, et avis citoyens collectés sur bien-dans-ma-ville.fr.\n\nLe pipeline de traitement tourne en local sur PySpark et passe à l'échelle sur Databricks Serverless en production, produisant 26 tables agrégées et 15 couches de cache GeoJSON stockées entre PostgreSQL 16 + PostGIS (relationnel & géospatial) et MongoDB 7 (documents de sentiment). Un modèle BERT multilingue évalue le sentiment des villes à partir de milliers d'avis utilisateurs, tandis qu'un modèle de séries temporelles Prophet génère des prévisions de prix à 12 mois par commune.\n\nLe frontend Next.js affiche des cartes choroplèthes et à bulles interactives via Mapbox, permettant aux utilisateurs de naviguer de la région nationale jusqu'à la commune individuelle avec des filtres en direct pour le prix, l'accessibilité financière, la note DPE et le score de sentiment. Le déploiement en production cible Kubernetes sur AWS, avec Docker Compose pour le développement local.",
  },
  kubequest: {
    description:
      "Cluster Kubernetes de production sur AWS avec GitOps via ArgoCD, déploiements progressifs sans interruption, stack d'observabilité complète Prometheus/Grafana/Loki, et sauvegardes nocturnes automatisées.",
    long_description:
      "KubeQuest est un projet d'infrastructure cloud de niveau production démontrant le cycle de vie DevOps complet pour une application Laravel conteneurisée.\n\nLe cluster tourne sur 4 instances AWS EC2 t4g.medium (ARM64 Graviton) en eu-west-3 : un control plane avec IP élastique, deux nœuds worker, et un nœud de monitoring dédié. Le trafic entre via un contrôleur nginx-ingress avec HTTPS Let's Encrypt automatique grâce à cert-manager.\n\nLe GitOps est géré par ArgoCD selon le pattern « App of Apps » — chaque changement d'infrastructure passe par Git, offrant une traçabilité complète et un rollback en une commande. GitHub Actions construit les images Docker à chaque commit, les pousse vers GHCR, et met à jour le fichier de valeurs Helm ; ArgoCD détecte le changement et exécute une mise à jour progressive sans interruption (maxUnavailable: 0).\n\nLa stack d'observabilité (kube-prometheus-stack) tourne sur son propre nœud : Prometheus collecte les métriques depuis kubelet, node-exporter et kube-state-metrics ; Grafana visualise les tableaux de bord ; Loki + Promtail centralisent tous les logs des pods. OPA Gatekeeper applique les politiques de contrôle d'admission. Des CronJobs nocturnes exportent MySQL vers MinIO (compatible S3), et Velero sauvegarde tous les manifestes Kubernetes pour une reprise après sinistre complète.",
  },
  visiobook: {
    description:
      "Plateforme IA qui transforme n'importe quel texte — roman, PDF, manuscrit — en VisioBook animé, orchestrant analyse sémantique par LLM, génération d'images FLUX et animation LTX-Video à travers plus de 10 microservices indépendants.",
    long_description:
      "Visiobook est une plateforme IA en production (projet Epitech ESP) qui transforme du contenu écrit en vidéo animée à regarder — pensez à un roman graphique qui prend vie. Un utilisateur télécharge un PDF, un DOCX ou un document scanné ; la plateforme en extrait le texte, le fait passer par un pipeline d'analyse LLM pour en extraire les personnages, les scènes, les arcs narratifs et le sentiment ; puis génère des illustrations sur mesure pour chaque scène et les anime en une vidéo VisioBook finale.\n\nLe backend est réparti sur plus de 10 microservices indépendants communiquant via NATS JetStream : un orchestrateur de projet NestJS/TypeScript gère le workflow multi-étapes ; un service d'analyse IA en FastAPI fait tourner Mistral Ministral-3B via vLLM pour l'extraction sémantique ; un service de génération de médias en FastAPI pilote ComfyUI sur GPU (RunPod) pour produire des images de référence de personnages (FLUX.1-dev), des illustrations de scènes (FLUX Redux pour la cohérence visuelle), et des animations (LTX-Video 2.3 22B en deux passes avec amélioration de prompt via Gemma 3). Un service d'ingestion de contenu gère l'OCR (Tesseract), le parsing PDF et le découpage intelligent du texte. L'infrastructure tourne sur Kubernetes avec Helm + Istio, l'inférence GPU étant accessible via VPN Tailscale.\n\nLes utilisateurs interagissent via une application mobile native Flutter (iOS + Android) avec un design glassmorphism et 795 tests unitaires/widgets, ou via le portail web. Les abonnements et quotas sont gérés via Stripe. La plateforme est en production live sur visiobook.cloud.",
  },
  criptoviz: {
    description:
      "Tableau de bord d'analyse crypto en temps réel avec streaming de prix WebSocket depuis Binance, stockage de séries temporelles TimescaleDB, graphiques en chandelles multi-période, et analyse de sentiment NLP bilingue sur l'actualité crypto en direct.",
    long_description:
      "CriptoViz est une plateforme d'analyse en microservices pour les marchés de cryptomonnaies. Quatre services Python indépendants tournent derrière RabbitMQ : un scraper ingère les données depuis les WebSockets Binance, CoinGecko et NewsAPI ; un service d'analytics calcule les agrégats OHLCV et les indicateurs techniques (SMA 20/50/200, EMA 12/26, RSI, MACD, Bollinger Bands, ATR) ; un service de diffusion WebSocket distribue les mises à jour en temps réel aux clients ; et un service de sentiment évalue les titres d'actualité avec un pipeline NLP hybride français/anglais (lexique personnalisé + repli VADER avec détection automatique de langue).\n\nLes données atterrissent dans TimescaleDB avec des agrégats continus sur 7 périodes (1 minute à 1 semaine) pour BTC, ETH, SOL, ADA et DOT. Le frontend React 19 + TypeScript affiche des graphiques en chandelles en direct via Recharts, un fil d'actualité en direct avec badges de sentiment, et des superpositions multi-indicateurs — le tout se mettant à jour en temps réel sans rafraîchissement de page. La stack complète démarre avec une seule commande docker-compose.",
  },
  "travel-order-disorder": {
    description:
      "Pipeline NLP multilingue qui extrait les villes d'origine et de destination à partir de demandes de voyage en langage naturel et calcule les itinéraires ferroviaires optimaux via une base de données graphe Neo4j — avec saisie vocale optionnelle.",
    long_description:
      "Travel Order Disorder est un système NLP de bout en bout qui comprend les demandes de voyage écrites (ou parlées) en français ou en anglais, en extrait les entités de villes pertinentes, et retourne des itinéraires ferroviaires optimaux.\n\nLa couche NLP utilise un modèle DistilBERT multilingue affiné pour la reconnaissance d'entités nommées, appuyé par CamemBERT pour les cas spécifiques au français et spaCy comme solution de repli légère. L'orchestrateur gère trois modes de saisie : CLI interactif, traitement par lot CSV, et saisie vocale optionnelle via OpenAI Whisper.\n\nLes entités extraites sont transmises à une API Express.js qui interroge une base de données graphe Neo4j contenant les nœuds de gares et les arêtes de trajets. Le graphe retourne des itinéraires complets avec distance, durée et arrêts intermédiaires. Les résultats sont exportés en JSON ou CSV avec des scores de confiance et les raisons de rejet pour les demandes invalides.\n\nTout tourne dans Docker Compose — l'instance Neo4j, l'API TypeScript, et le service NLP Python — rendant la stack complète reproductible en une seule commande.",
  },
  zoidberg: {
    description:
      "Pipeline de deep learning qui détecte et classifie automatiquement la pneumonie à partir de radiographies thoraciques, comparant DenseNet-121, VGG16, ResNet50 et EfficientNetB0 avec explicabilité Grad-CAM.",
    long_description:
      "Zoidberg est un projet d'imagerie médicale axé sur la détection automatisée de la pneumonie à partir de radiographies thoraciques, distinguant pneumonie bactérienne et virale grâce au transfer learning sur des CNN pré-entraînés.\n\nLe pipeline commence par une EDA et un prétraitement approfondis — standardisation des dimensions d'image, application d'un split train/val/test 80/10/10, et gestion du déséquilibre de classes important via des stratégies d'augmentation ciblées (rotations, flips, variation de luminosité). Quatre architectures sont entraînées et comparées en parallèle : DenseNet-121, VGG16, ResNet50 (incluant une variante multiclasse), et EfficientNetB0.\n\nEfficientNetB0 inclut une visualisation des cartes d'activation Grad-CAM, produisant des heatmaps qui mettent en évidence les régions de la radiographie les plus influentes dans la prédiction — un aspect essentiel pour l'interprétabilité clinique et la confiance. Un rapport technique détaillé en français documente la méthodologie, les choix d'hyperparamètres et les résultats comparatifs pour tous les modèles et variantes de jeu de données.",
  },
  timemanager: {
    description:
      "Application de suivi du temps full-stack avec une API REST construite en Elixir/Phoenix, une SPA Vue.js, authentification JWT, et un pipeline de monitoring propulsé par Prometheus et Logstash.",
    long_description:
      "TimeManager est une application de gestion du temps orientée production. Elle démontre une séparation propre entre une couche API haute performance et un frontend réactif, le tout orchestré avec Docker Compose.\n\nLe backend est une API REST Elixir/Phoenix gérant les utilisateurs, les pointages (début/fin de session) et les agrégats d'heures travaillées, avec une authentification basée sur JWT sécurisant tous les endpoints. Le frontend Vue.js fournit une SPA responsive permettant aux employés et managers d'enregistrer leurs sessions de travail, consulter l'historique et suivre le temps.\n\nL'infrastructure est gérée via Docker Compose avec des configurations dev et production séparées. Nginx agit comme reverse proxy routant le trafic API et frontend. Un pipeline Logstash traite et achemine les logs applicatifs, tandis que Prometheus collecte les métriques pour la visibilité opérationnelle — donnant au projet une empreinte d'observabilité digne de la production, au-delà d'une application étudiante typique.",
  },
  wino: {
    description:
      "Marketplace bidirectionnelle connectant les amateurs de vin aux cavistes proposant des dégustations organisées — construite avec Ruby on Rails et déployée en direct sur Heroku.",
    long_description:
      "WINO est une marketplace qui met en relation les amateurs de vin en quête de découverte avec des cavistes proposant des sessions de dégustation organisées. La plateforme gère le parcours de réservation complet : les cavistes publient des expériences avec dates et capacité ; les explorateurs parcourent, filtrent et réservent ; les deux parties gèrent leur profil et leur historique via une interface Rails MVC épurée.\n\nConstruit durant le bootcamp intensif du Wagon, le projet démontre le développement produit full-stack, de la modélisation du domaine et la conception de base de données jusqu'au style SCSS, à l'interactivité Stimulus JS et au déploiement cloud. L'instance Heroku en direct sert du trafic réel et inclut l'hébergement d'images Cloudinary pour les photos de cavistes et d'expériences.\n\nWINO va bien au-delà d'une application tutoriel — couvrant l'authentification, l'autorisation basée sur les rôles, l'upload de fichiers, les mailers, et une UI responsive soignée.",
  },
  slowwave: {
    description:
      "Application web de portfolio photographique avec galeries dynamiques et design minimaliste, construite avec Ruby on Rails.",
    long_description:
      "Slowwave est un portfolio photographique personnel. Il sert de vitrine pour un travail photographique couvrant les genres voyage, street et documentaire.\n\nConstruit sur Ruby on Rails, l'application comprend un système de galerie organisé, un design minimaliste piloté par SCSS avec des choix typographiques soignés, et un outillage frontend moderne.\n\nLe projet a été poussé vers une qualité de production avec une configuration de déploiement Heroku, une optimisation des images, et une structure d'URL propre, davantage axé sur l'artisanat et la présentation que sur l'étendue fonctionnelle.",
  },
  creativehub: {
    description:
      "Marketplace bidirectionnelle connectant designers et opportunités freelance avec des entreprises en recherche de propositions de design — construite avec Ruby on Rails.",
    long_description:
      "CreativeHub est un projet du bootcamp Le Wagon construit en équipe durant un sprint de développement intensif. La plateforme relie deux publics : les designers en recherche de leur prochaine mission freelance, et les entreprises ayant besoin de propositions de design pour leurs campagnes publicitaires et de branding.\n\nL'application suit un schéma classique de marketplace bidirectionnelle — les entreprises publient des briefs avec exigences et budget ; les designers parcourent, postulent et soumettent des propositions ; les deux parties gèrent leur activité via des tableaux de bord dédiés. Construit sur Ruby on Rails avec la stack de production rails-templates du Wagon, il propose une authentification Devise, des uploads d'images Cloudinary, un chat en temps réel et une interface responsive designée en SCSS.\n\nCreativeHub est un produit entièrement livré plutôt qu'un prototype — quelque chose que l'équipe a construit de bout en bout en quelques semaines.",
  },
  "trinity-food-market": {
    description:
      "Plateforme full-stack de gestion de marché alimentaire avec une API Node.js/Express, une SPA Vue.js, une orchestration Docker Compose pour les profils dev et production, et un support Android natif via Capacitor.",
    long_description:
      "Trinity Food Market est une application de marketplace alimentaire multiplateforme construite avec une séparation nette entre backend et frontend, tous deux conteneurisés et reliés via Docker Compose.\n\nLe backend expose une API REST construite sur Node.js, gérant l'inventaire, les commandes et la gestion des utilisateurs. Le frontend Vue.js fournit la SPA orientée client avec navigation de produits et parcours de commande. Un script de population de données permet à l'équipe d'alimenter la base de données depuis des fichiers JSON — utile pour les environnements de développement et de démonstration. Le projet est livré avec deux profils Docker Compose : dev (avec hot-reload) et prod (optimisé, prêt pour la production).\n\nUne fonctionnalité marquante est le support Android natif via Capacitor, qui enveloppe l'application web Vue.js dans un binaire Android natif — donnant au projet une véritable portée multiplateforme à partir d'une seule base de code.",
  },
  eventscraper: {
    description:
      "Réalisé comme test technique d'embauche, EventScraper est une plateforme d'agrégation d'événements qui scrape Eventbrite, TripAdvisor et Facebook pour centraliser les activités en un seul endroit, avec une carte interactive et un assistant IA Google Dialogflow pour les requêtes en langage naturel.",
    long_description:
      "EventScraper résout un vrai point de friction : les événements sont dispersés entre Eventbrite, TripAdvisor et Facebook, obligeant les utilisateurs à consulter trois plateformes. Cette application les agrège tous dans un flux unique et consultable, avec une superposition OpenStreetMap interactive montrant les emplacements des événements.\n\nLe backend est un service Python/Flask qui pilote les scrapers et expose une API REST. Le frontend Vue.js + Vuetify fournit une UI propre et responsive avec filtrage par catégorie, date et localisation. La fonctionnalité marquante est un assistant IA propulsé par Google Dialogflow qui permet aux utilisateurs de rechercher des événements en langage naturel (« Qu'est-ce qui se passe près de chez moi ce week-end ? ») — l'intention est analysée et traduite en filtres API.\n\nLe projet pose également les bases d'extensions futures : des intégrations GetYourGuide, Funbooker et Civitatis sont prévues, ainsi que l'authentification utilisateur et une couche de format de date unifiée à travers les sources scrapées.",
  },
  afpcontentmanager: {
    description:
      "Outil interne de gestion de contenu développé comme test technique d'embauche pour fluidifier le workflow éditorial et les opérations de contenu.",
    long_description:
      "AFP Content Manager est un outil interne construit comme démo pour l'Agence France-Presse, l'agence de presse internationale française. Le projet soutient les workflows d'opérations éditoriales et de contenu au sein de l'écosystème AFP.",
  },
  "arenamatrix-csv-uploader": {
    description:
      "Application web Rails qui ingère les exports CSV de réservations d'ArenaMatrix et les présente sous forme de tableau consultable et filtrable — avec packaging Docker et déploiement Render.",
    long_description:
      "ArenaMatrix CSV Uploader est un utilitaire ciblé construit pour relier les données de réservation ArenaMatrix à une interface web propre. Les utilisateurs téléchargent les exports CSV du système ArenaMatrix ; l'application Rails parse, stocke et affiche les enregistrements dans un tableau consultable et triable.\n\nLe projet est volontairement circonscrit — il résout un problème correctement plutôt que d'essayer d'être un CRM complet. La structure Rails MVC garde la logique de parsing et d'affichage propre. Un Dockerfile et une configuration render.yaml rendent le déploiement simple sur la plateforme Render.",
  },
}

// Returns `project` with description/long_description swapped to their
// French translation when `locale === 'fr'` and one exists, otherwise
// returns the project untouched (falls back to the API's English text).
export function localizeProject(project, locale) {
  if (!project || locale !== 'fr') return project
  const tr = projectTranslationsFr[project.slug]
  if (!tr) return project
  return {
    ...project,
    description: tr.description ?? project.description,
    long_description: tr.long_description ?? project.long_description,
  }
}
