import axios from 'axios'
import Vue from 'vue'
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
function login(username,password) {
	let data = axios.post('token/',{username,password})
	return data
}
function refresh(refreshcode){
	let data = axios.post('token/refresh/',{refresh:refreshcode})
	return data
}
function getuserinfo(id){
	let data = axios.get('ac/accounts/'+id)
	return data
}
export{
    login,
	refresh,
	getuserinfo
}