import React, { useEffect, useState } from 'react';
import { Job } from '../types/Jobs';
import axios from 'axios';

const JobList: React.FC = () => {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const response = await axios.get<Job[]>('http://localhost:8000/api/jobs/');
        setJobs(response.data.results);
      } catch (err) {
        setError('Failed to fetch jobs');
      } finally {
        setLoading(false);
      }
    };

    fetchJobs();
  }, []);

  if (loading) {
    return <p>Loading jobs...</p>;
  }

  if (error) {
    return <p className="text-red-500">{error}</p>;
  }

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Job Listings</h2>
      {jobs.length === 0 ? (
        <p>No jobs found.</p>
      ) : (
        <ul className="space-y-4">
          {jobs.map((job) => (
            <li key={job.id} className="p-4 border rounded shadow">
              <a href={job.url} className="text-xl font-semibold text-blue-600 hover:underline" target="_blank" rel="noopener noreferrer">
                {job.title}
              </a>
              {job.company && <p className="text-gray-700">{job.company}</p>}
              {job.salary && <p className="text-green-600">Salary: {job.salary}</p>}
              {job.location && <p className="text-gray-500">Location: {job.location}</p>}
              <p className="text-sm text-gray-400">{new Date(job.date_published).toLocaleString()}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default JobList;
