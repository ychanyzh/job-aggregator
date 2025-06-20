export async function fetchJobs({ search = '', page = 1 } = {}) {
  const params = new URLSearchParams({
    search: String(search),
    page: String(page),
  });

  const response = await fetch(`/api/jobs/?${params.toString()}`);
  if (!response.ok) {
    throw new Error('Failed to fetch jobs');
  }
  return response.json();
}
