import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000',  // URL of the server
});

export default api;