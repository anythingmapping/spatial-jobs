<template>
  <div class="jobs-container">
    <h1>Spatial Jobs</h1>
    <div v-if="loading" class="loading">Loading jobs...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="jobs-grid">
      <div v-for="job in jobs" :key="job.id" class="job-card">
        <h2 class="job-title">{{ job.title }}</h2>
        <div class="job-company">{{ job.company }}</div>
        <div class="job-location">📍 {{ job.location }}</div>
        <p class="job-description">{{ job.description }}</p>
        <div class="job-footer">
          <span class="job-date">Posted: {{ job.posted_date }}</span>
          <button class="apply-button">Apply Now</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const API_URL = import.meta.env.MODE === 'development' 
  ? 'http://localhost:8000'
  : 'https://anythingmapping.pythonanywhere.com';

const jobs = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await fetch(`${API_URL}/api/jobs`)
    if (!response.ok) throw new Error('Failed to fetch jobs')
    const data = await response.json()
    jobs.value = data.jobs
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.jobs-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.jobs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.job-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s ease;
}

.job-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.job-title {
  margin: 0;
  color: #2c3e50;
  font-size: 1.25rem;
}

.job-company {
  color: #34495e;
  font-weight: 500;
  margin-top: 8px;
}

.job-location {
  color: #7f8c8d;
  margin-top: 8px;
}

.job-description {
  margin: 16px 0;
  line-height: 1.5;
}

.job-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 16px;
}

.job-date {
  color: #95a5a6;
  font-size: 0.9rem;
}

.apply-button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.apply-button:hover {
  background-color: #2980b9;
}

.loading, .error {
  text-align: center;
  padding: 40px;
  color: #7f8c8d;
}

.error {
  color: #e74c3c;
}
</style> 