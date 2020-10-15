import axios from 'axios'
import Vue from 'vue'
// axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
function getcomment(ContentType,ObjectId,CommentUrl){
	let data = axios.get(CommentUrl,{ params: 
		{ 
			content_type: ContentType,
			object_id: ObjectId 
		,},},)
	return data
}
function deletecomment(CommentUrl,CommentObject){
	let data = axios.delete(CommentUrl + CommentObject.id + '/')
	return data
}
function sendcomment(ContentType, ObjectId, Body, Author, Root, Parent, ReplyTo,CommentUrl){
	let postData = {
		"content_type": parseInt(ContentType),
		"object_id": parseInt(ObjectId),
		"body":Body,
		"author":parseInt(Author),
		"root":Root,
		"parent":Parent,
		"reply_to":ReplyTo
	}
	let data = axios.post(CommentUrl, postData)
	return data
}
export{
	getcomment,
	sendcomment,
	deletecomment
}