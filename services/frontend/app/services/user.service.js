import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/api/auth/';

class UserService {
  getPublicContent() {
    const res = axios.get(API_URL + 'all')
    console.log(res)
    return res;
    // return axios.get(API_URL + 'all');
    // return axios.get(API_URL + 'user', { headers: authHeader() });
  }

  getUserBoard() {
    return axios.get(API_URL + 'user', { headers: authHeader() });
  }

  getModeratorBoard() {
    return axios.get(API_URL + 'mod', { headers: authHeader() });
  }

  getAdminBoard() {
    return axios.get(API_URL + 'admin', { headers: authHeader() });
  }
}

export default new UserService();