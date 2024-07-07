// Create instance of axios

import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "https://api.example.com", // Your API base URL
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
