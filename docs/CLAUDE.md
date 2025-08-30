# CASP Project Documentation Guide

## Project Overview
CASP is a health and wellness application designed to help users develop self-awareness about their health patterns through observation, compassion, and gradual behavior change. The application philosophy centers on the principle: "None of it is your fault. It is all your responsibility."

## Document Structure

### 1. DESIGN_DOCUMENT.md
**Purpose:** Core philosophical foundation and problem analysis
**Contents:**
- The Eight Core Health Challenges (knowledge-behavior gap, shame spiral, etc.)
- The Comfort-Health Paradox (how unhealthy behaviors provide psychological support)
- Solution architecture including observational mindfulness and pattern recognition
- Evaluation framework and success metrics

**Use this when:** Understanding the fundamental problems the app solves and the philosophical approach

### 2. BOOK.md
**Purpose:** Comprehensive narrative explanation for general audience
**Contents:**
- 9 chapters covering philosophy through implementation
- Detailed exploration of human health paradoxes
- Stories and examples to illustrate concepts
- Bridge between philosophy and practical application

**Use this when:** Needing deep context or explaining the project to stakeholders

### 3. DESIGN_GUIDE.md
**Purpose:** Practical implementation guide for developers
**Contents:**
- Core design principles and anti-patterns
- User experience specifications
- Language guidelines ("I noticed..." vs "You should...")
- Crisis management protocols
- Technical implementation priorities

**Use this when:** Making design decisions or implementing features

### 4. APPLICATION_EXPERIENCE_DESIGN.md
**Purpose:** Detailed user experience design and journey mapping
**Contents:**
- 7 Epics with specific user stories
- Exact interface copy and interaction flows
- Emotional journey map from arrival to independence
- Visual and interaction design principles

**Use this when:** Building user interfaces or designing user interactions

### 5. IMPLEMENTATION_ROADMAP.md
**Purpose:** Development timeline and technical specifications
**Contents:**
- 36-week development plan in 5 phases
- Database schemas and technical architecture
- Sprint-by-sprint feature development
- MVP definition and success metrics
- Risk mitigation strategies

**Use this when:** Planning development sprints or making technical decisions

## Key Principles to Remember

### Core Philosophy
- Users are not broken and don't need fixing
- Health struggles are not moral failures
- Change happens through awareness, not force
- The app should eventually become unnecessary

### Design Approach
- Always reduce shame, never increase it
- Observation before action
- Patterns over performance
- Context over content
- Progress over perfection

### Technical Stack
- **Frontend:** Django templates with HTMX 2 + Bootstrap 5
- **Backend:** Django 5.x + PostgreSQL + Redis
- **Platform:** Progressive Web App (PWA)
- **Deployment:** Responsive web-first, cross-platform

### Technical Priorities
1. Compassionate onboarding (responsive design)
2. Adaptive interface based on user capacity (HTMX interactions)
3. Pattern recognition without judgment (Django backend)
4. PWA capabilities (offline, installable)
5. Crisis detection and support
6. Community through shared patterns
7. Gradual independence with platform evaluation

### Language Rules
**Always use:**
- "I noticed..."
- "I'm curious..."
- "Would you like..."

**Never use:**
- "You should..."
- "You failed..."
- "Try harder"

## Development Workflow

1. **New Feature Development:**
   - Check DESIGN_GUIDE.md for principles
   - Reference APPLICATION_EXPERIENCE_DESIGN.md for UX patterns
   - Follow IMPLEMENTATION_ROADMAP.md for technical approach
   - Ensure responsive design for mobile, tablet, desktop

2. **User Interface Creation:**
   - Use exact copy from APPLICATION_EXPERIENCE_DESIGN.md
   - Apply visual principles from DESIGN_GUIDE.md
   - Implement with HTMX 2 interactions and Bootstrap 5 components
   - Ensure crisis mode adaptations are implemented
   - Test across all device sizes

3. **Pattern Detection Features:**
   - Review DESIGN_DOCUMENT.md for philosophical approach
   - Implement schemas from IMPLEMENTATION_ROADMAP.md
   - Present patterns as observations, not prescriptions
   - Use Django backend for ML/pattern processing

4. **PWA Development:**
   - Implement service workers for offline functionality
   - Add web app manifest for installability
   - Test push notifications (where supported)
   - Optimize for mobile performance

## Success Metrics
- Decreasing time between relapse and return
- Users developing their own experiments
- Gradual reduction in app dependency
- Pattern awareness increase
- Crisis support utilization when needed

## Platform Strategy
- **Phase 1:** Web-first with PWA capabilities (serves all users)
- **Phase 2:** Enhanced mobile experience with native-like interactions
- **Phase 3:** Evaluate usage data to decide on native app development
- **Decision Point:** Week 32 - Continue web-first or add React Native based on user engagement patterns

## Remember
The ultimate goal is not to keep users engaged forever, but to help them develop such strong self-awareness that they no longer need the app. We're building a ladder, not a crutch. The web-first approach allows us to serve all users (mobile, tablet, desktop) from day one while maintaining the option to add native apps based on real usage data.