import axios from 'axios'
import Vue from 'vue'
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
function getarticlelist() {
	let data = axios.get('a/articles')
	return data
}
function getarticledetail(id) {
	let data = axios.get("a/articles/"+id)
	return data
}
export{
	getarticlelist,
	getarticledetail,
}