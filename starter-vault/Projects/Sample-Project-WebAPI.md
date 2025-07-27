# Sample Project: Build a Web API

This is an example project structure to demonstrate how to use the Brain system for project management.

## 📋 Project Overview

**Name**: SampleAPI
**Type**: Web Application
**Status**: Planning
**Created**: 2025-07-27

## 🎯 Goals

1. Build a RESTful API with authentication
2. Implement CRUD operations
3. Add comprehensive testing
4. Deploy to production

## 📊 Project Memory

```
brain_remember {
  "key": "project_sampleapi_overview",
  "value": {
    "name": "SampleAPI",
    "description": "RESTful API with authentication",
    "tech_stack": ["Node.js", "Express", "PostgreSQL"],
    "status": "planning",
    "team_size": 1,
    "timeline": "4 weeks"
  },
  "type": "project"
}
```

## ✅ Tasks

```
todo_add {
  "project": "sampleapi",
  "title": "Design API endpoints",
  "description": "Define all RESTful endpoints and their schemas",
  "priority": "high"
}

todo_add {
  "project": "sampleapi",
  "title": "Setup development environment",
  "description": "Initialize Node.js project with Express",
  "priority": "high"
}

todo_add {
  "project": "sampleapi",
  "title": "Implement authentication",
  "description": "JWT-based auth with refresh tokens",
  "priority": "critical"
}
```

## 🏗️ Architecture Decisions

### Decision 1: Database Choice
**Date**: 2025-07-27
**Decision**: Use PostgreSQL
**Reasoning**: 
- Strong consistency requirements
- Complex relationships between entities
- Good Node.js support

```
brain_remember {
  "key": "project_sampleapi_decision_database",
  "value": {
    "decision": "PostgreSQL",
    "alternatives_considered": ["MongoDB", "MySQL"],
    "reasoning": "ACID compliance and relationship support",
    "date": "2025-07-27"
  }
}
```

## 📁 File Structure

```
/sampleapi
  /src
    /controllers
    /models
    /routes
    /middleware
    /utils
  /tests
  /docs
  .env.example
  package.json
  README.md
```

## 🔧 Development Notes

### Setup Commands
```
brain_execute {
  "code": "mkdir -p sampleapi/{src/{controllers,models,routes,middleware,utils},tests,docs}",
  "language": "shell",
  "description": "Create project structure"
}
```

### Dependencies
```json
{
  "express": "^4.18.0",
  "jsonwebtoken": "^9.0.0",
  "bcrypt": "^5.1.0",
  "pg": "^8.11.0",
  "joi": "^17.9.0"
}
```

## 📝 Session Notes

### Session 1: Project Setup (2025-07-27)
- Created project structure
- Defined initial requirements
- Set up task tracking
- Made technology decisions

### Session 2: [Future]
- Will implement basic Express server
- Set up database connection
- Create first endpoint

## 🔗 Resources

- [Express Documentation](https://expressjs.com/)
- [JWT Best Practices](https://example.com)
- [PostgreSQL Node.js Guide](https://example.com)

## 💡 Patterns to Remember

```
brain_remember {
  "key": "pattern_express_error_handler",
  "value": {
    "description": "Global error handling middleware",
    "code": "app.use((err, req, res, next) => { ... })",
    "usage": "Place at end of middleware stack"
  },
  "type": "pattern"
}
```

## 🚀 Deployment Checklist

- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Tests passing
- [ ] Documentation complete
- [ ] Security audit done
- [ ] Performance tested

## 📊 Progress Tracking

```
state_set {
  "key": "sampleapi_progress",
  "value": {
    "phase": "planning",
    "completion": 0.1,
    "next_milestone": "Basic server running"
  },
  "category": "project"
}
```

---

This sample demonstrates:
- Using memories for project data
- Task management with todos
- Decision documentation
- Code execution for setup
- Pattern storage for reuse
- Progress tracking with state
