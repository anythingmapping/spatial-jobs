## To run locally
yarn dev within /frontend
python flask_app.py

## DEV PLAN

### Phase 1: Local SQLite Setup
1. Create SQLite database models + install migrations requirements in pip 
2. Setup local database and run with migrated data
3. Add Database Admin Interface
   - Basic CRUD operations
   - Job status management
   - Data validation

### Phase 2: Production Database
1. PythonAnywhere Database Setup
   - Configure SQLite in production
   - Create backup strategy
   - Setup automated migrations
   - Test with demo data

2. Database Management
   - Add backup/restore scripts
   - Setup periodic backups
   - Add data validation
   - Error handling

### Phase 3: STAC Implementation
1. STAC Integration
   - Define STAC item structure
   - Create STAC catalog
   - Link jobs to STAC items
   - Add spatial search capabilities

2. STAC Features
   - Add map visualization
   - Implement STAC API endpoints
   - Add spatial filtering
   - Create STAC browser interface

### Phase 4: Testing & Documentation
1. Testing
   - Unit tests for database operations
   - Integration tests for STAC
   - API endpoint testing
   - Frontend testing

2. Documentation
   - API documentation
   - Database schema
   - STAC implementation details
   - Deployment guides




