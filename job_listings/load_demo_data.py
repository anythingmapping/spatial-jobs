from datetime import datetime
from flask import Flask
from job_listings.models.models import db, Job

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobs.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Sample jobs data - we can move this to a database later
JOBS = [
    {
        "id": 1,
        "title": "GIS Analyst",
        "company": "Spatial Solutions NZ",
        "location": "Auckland, NZ",
        "coordinates": [174.7633, -36.8485],  # Auckland
        "description": "Looking for an experienced GIS analyst for urban planning projects...",
        "posted_date": "2024-01-22",
        "remote": False,
    },
    {
        "id": 2,
        "title": "Remote Sensing Specialist",
        "company": "Earth Data NZ",
        "location": "Wellington, NZ",
        "coordinates": [174.7762, -41.2866],  # Wellington
        "description": "Seeking a specialist in satellite imagery analysis for environmental monitoring...",
        "posted_date": "2024-01-21",
        "remote": True,
    },
    {
        "id": 3,
        "title": "Geospatial Developer",
        "company": "Tech Kiwi Ltd",
        "location": "Christchurch, NZ",
        "coordinates": [172.6362, -43.5321],  # Christchurch
        "description": "Python developer with strong background in spatial databases...",
        "posted_date": "2024-01-20",
        "remote": False,
    },
    {
        "id": 4,
        "title": "LiDAR Technician",
        "company": "Survey Plus",
        "location": "Hamilton, NZ",
        "coordinates": [175.2793, -37.7870],  # Hamilton
        "description": "Experienced LiDAR data processing specialist needed...",
        "posted_date": "2024-01-19",
        "remote": False,
    },
    {
        "id": 5,
        "title": "Cartographer",
        "company": "Maps & More",
        "location": "Dunedin, NZ",
        "coordinates": [170.5036, -45.8788],  # Dunedin
        "description": "Creating beautiful and accurate maps for tourism sector...",
        "posted_date": "2024-01-18",
        "remote": False,
    },
    {
        "id": 6,
        "title": "Environmental GIS Specialist",
        "company": "EcoMap NZ",
        "location": "Tauranga, NZ",
        "coordinates": [176.1651, -37.6878],  # Tauranga
        "description": "Environmental impact assessment and mapping...",
        "posted_date": "2024-01-17",
        "remote": False,
    },
    {
        "id": 7,
        "title": "Spatial Data Scientist",
        "company": "Data Insights Ltd",
        "location": "Wellington, NZ",
        "coordinates": [174.7762, -41.2866],  # Wellington
        "description": "Analyzing spatial patterns in urban development...",
        "posted_date": "2024-01-16",
        "remote": True,
    },
    {
        "id": 8,
        "title": "UAV Mapping Specialist",
        "company": "Drone Survey NZ",
        "location": "Napier, NZ",
        "coordinates": [176.9120, -39.4928],  # Napier
        "description": "Drone mapping and photogrammetry expert needed...",
        "posted_date": "2024-01-15",
        "remote": False,
    },
    {
        "id": 9,
        "title": "GIS Consultant",
        "company": "Geo Consulting Group",
        "location": "Nelson, NZ",
        "coordinates": [173.2840, -41.2706],  # Nelson
        "description": "Consulting on GIS implementation for local government...",
        "posted_date": "2024-01-14",
        "remote": False,
    },
    {
        "id": 10,
        "title": "Spatial Database Administrator",
        "company": "Data Systems Ltd",
        "location": "Auckland, NZ",
        "coordinates": [174.7633, -36.8485],  # Auckland
        "description": "Managing and optimizing spatial databases...",
        "posted_date": "2024-01-13",
        "remote": False,
    },
    {
        "id": 11,
        "title": "Marine GIS Specialist",
        "company": "Ocean Maps NZ",
        "location": "New Plymouth, NZ",
        "coordinates": [174.0752, -39.0556],  # New Plymouth
        "description": "Mapping marine ecosystems and coastal zones...",
        "posted_date": "2024-01-12",
        "remote": False,
    },
    {
        "id": 12,
        "title": "Cadastral Surveyor",
        "company": "Land Survey Pro",
        "location": "Palmerston North, NZ",
        "coordinates": [175.6111, -40.3556],  # Palmerston North
        "description": "Property boundary surveys and legal documentation...",
        "posted_date": "2024-01-11",
        "remote": False,
    },
]


def load_demo_data():
    with app.app_context():
        # Clear existing data
        Job.query.delete()

        # Load demo jobs
        for job_data in JOBS:
            job = Job(
                title=job_data["title"],
                company=job_data["company"],
                location=job_data["location"],
                coordinates=job_data["coordinates"],
                description=job_data["description"],
                remote=job_data.get("remote", False),
                posted_date=datetime.strptime(job_data["posted_date"], "%Y-%m-%d"),
                status="active",
            )
            db.session.add(job)

        db.session.commit()
        print(f"Loaded {len(JOBS)} jobs into database")


if __name__ == "__main__":
    load_demo_data()
