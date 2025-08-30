# Tend

A compassionate health awareness application that helps users understand their patterns through observation, not judgment.

## Philosophy

Tend is built on the principle: **"None of it is your fault. It is all your responsibility."**

We believe that:
- Users are not broken and don't need fixing
- Health struggles are not moral failures
- Everyone is doing their best given their circumstances
- Change happens through awareness, not force
- The ultimate goal is to help users become independent of the app

## What Tend Does

Tend helps users:
- **Observe** their health patterns without judgment
- **Understand** connections between behaviors, context, and outcomes
- **Experiment** with tiny changes based on their unique patterns
- **Recover** gracefully from setbacks
- **Graduate** to self-awareness and independence

## Technical Overview

### Stack
- **Frontend:** Django templates with HTMX 2 + Bootstrap 5
- **Backend:** Django 5.x + PostgreSQL + Redis
- **Platform:** Progressive Web App (PWA)
- **Deployment:** Responsive web-first, cross-platform

### Key Features
- Gentle, adaptive onboarding
- Daily energy/mood check-ins
- Pattern recognition and visualization
- Micro-experiments based on personal patterns
- Crisis detection and support
- Community through shared patterns (not demographics)
- Gradual independence as success metric

## Project Structure

```
tend/
├── docs/                     # Design documentation
├── tend_project/            # Django project root
│   ├── manage.py
│   ├── tend/               # Main Django app
│   ├── apps/               # Feature apps
│   │   ├── core/          # Core functionality
│   │   ├── patterns/      # Pattern detection
│   │   ├── users/         # User management
│   │   └── observations/  # Data collection
│   ├── static/            # Static files
│   ├── templates/         # Django templates
│   └── tests/             # Test suite
├── docker-compose.yml      # Development environment
└── requirements.txt        # Python dependencies
```

## Development Setup

### Prerequisites
- Python 3.11+
- Docker and Docker Compose
- Git

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cair-mun/tend.git
   cd tend
   ```

2. **Start development environment:**
   ```bash
   docker-compose up -d
   ```

3. **Run migrations:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create superuser:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Visit the application:**
   - Web app: http://localhost:8000
   - Admin: http://localhost:8000/admin

### Manual Setup (Alternative)

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Run migrations:**
   ```bash
   cd tend_project
   python manage.py migrate
   ```

5. **Start development server:**
   ```bash
   python manage.py runserver
   ```

## Design Philosophy in Practice

### User Experience Principles
- **Observation Before Action** - Always encourage noticing before changing
- **Shame Reduction** - Every interaction should reduce shame, never increase it
- **Context Over Content** - Remember situational factors and environmental influences
- **Progress Over Perfection** - Celebrate small consistencies, focus on sustainable patterns

### Language Guidelines
**Always use:**
- "I noticed..."
- "I'm curious..."
- "Would you like..."

**Never use:**
- "You should..."
- "You failed..."
- "Try harder"

## Development Workflow

1. Check design documents in `docs/` folder for principles and patterns
2. Follow responsive design for mobile, tablet, desktop
3. Use HTMX 2 for smooth, app-like interactions
4. Implement features with Django backend + Bootstrap 5 frontend
5. Test across all device sizes
6. Ensure crisis mode adaptations work properly

## Contributing

1. Read the design documents in `docs/` folder
2. Follow the established patterns and principles
3. Write tests for new features
4. Ensure responsive design works on all devices
5. Submit pull requests with clear descriptions

## Success Metrics

- Decreasing time between relapse and return
- Users developing their own experiments
- Gradual reduction in app dependence
- Pattern awareness increase
- Crisis support utilization when needed

## License

[To be determined - recommend MIT or Apache 2.0]

## Support

For questions or support, please open an issue on GitHub.

---

*Remember: We're building a ladder, not a crutch. The highest honor would be a user saying: "This app taught me to understand myself so well that I don't need it anymore. But I'm grateful it was there when I did."*