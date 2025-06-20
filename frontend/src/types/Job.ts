export interface Job {
  id: number;
  title: string;
  url: string;
  company?: string;
  salary?: string;
  description?: string;
  location?: string;
  experience?: string;
  source: string;
  is_active: boolean;
  date_published: string; // або Date, якщо парсиш
}