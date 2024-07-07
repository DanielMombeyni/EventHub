import axiosInstance from "./axiosInstance";

export const fetchEvents = async () => {
  const response = await axiosInstance.get("/events");
  return response.data;
};

export const fetchEventById = async (id: string) => {
  const response = await axiosInstance.get(`/events/${id}`);
  return response.data;
};
