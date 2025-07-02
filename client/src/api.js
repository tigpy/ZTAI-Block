import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  // Only add this if you're using cookies or auth sessions
  // withCredentials: true
});

export default API;
