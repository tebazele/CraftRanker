import axios from "axios";
import { baseURL } from "../env.js";

const api = axios.create({
  baseURL: baseURL
});




// const sessionStorage = Window.sessionStorage

if (sessionStorage.loginToken) {
  api.defaults.headers.common['Authorization'] = sessionStorage.loginToken;
}

export default api;