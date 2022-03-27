import axios from 'axios';

const url = "http://localhost:8000/api";

export const register = (data) => {
    return axios.post(url = "/users/register/", data);
};

export const login = (data) => {
    return axios.post(url + '/users/login/', data);
};  

export const courseSearch = () => {
    return axios.get(url + '/courses/');
};

export const courseGetSingle = (courseId) => {
    return axios.get(url + '/courses/course/' + courseId + '/');
};

export const courseCreate = (data) => {
    return axios.post(url + '/courses/create/', data);  
};

export const courseUpdate = (courseId) => {
    return axios.put(url + '/courses/update/ ' + courseId + '/');
};

export const courseDelete = (courseId) => {
    return axios.delete(url + '/courses/delete/' + courseId + '/');
};

export const sectionSearch = () => {
    return axios.get(url + "/sections/");
};

export const sectionGetSingle = (sectionId) => {
    return axios.get(url + "/sections/section/" + sectionId + '/');
};

export const sectionCreate = (data) => {
    return axios.post(url + '/sections/create/', data);
};

export const sectionUpdate = (sectionId) => {
    return axios.put(url + '/sections/update' + sectionId + '/');
};

export const sectionDelete = (sectionId) => {
    return axios.delete(url + '/sections/delete/' + sectionId + '/');  
};

export const lessonSearch = () => {
    return axios.get(url + '/lessons/');
};

export const lessonGetOne = (lessonId) => {
    return axios.get(url + '/lessons/lesson/' + lessonId + '/');
};

export const lessonCreate = (data) => {
    return axios.post(url + '/lessons/create/', data);
};

export const lessonUpdate = (lessonId) => {
    return axios.put(url + '/lessons/update/' + lessonId + '/');
};

export const lessonDelete = (lessonId) => {
    return axios.delete(url + '/lessons/delete/' + lessonId + '/');
};