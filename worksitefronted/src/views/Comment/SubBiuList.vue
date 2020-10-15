<template>
	<div>
		
		<v-row v-for="(reply,index) in comment" class="replylayer">
			<v-col cols='12' class="replylayerleft">
				<v-list-item-avatar class="replyavatar">
					<v-img :src="reply.author_avatar">
					</v-img>
				</v-list-item-avatar>
				<div class="replylayerup">
					{{reply.comment_author}} <span>回复给</span> {{reply.reply_author}} {{reply.create_at | dateFormat}}
				</div>
				<hr>
				<div class="replylayerdown">
					<div>
						<p>{{reply.body}}</p> 
						<v-btn text>点赞</v-btn>
						<v-btn text>踩他</v-btn>
						<v-btn text @click="toreply(reply)">回复</v-btn>
						<v-btn text>举报</v-btn>
						<v-btn text @click="todelete(reply)" v-if="loginId === reply.author">删除</v-btn>
					</div>
					<BiuBox v-show="showReplyId === reply.id" :CommentLayer="ReplyLayer"></BiuBox>
				</div>
			</v-col>
			<div class="sub"><SubBiuList :comment="reply.replies" v-if="reply.author_avatar"></SubBiuList></div>
		</v-row>
	</div>
</template>

<script>
	import BiuBox from '@/views/Comment/BiuBox.vue'
	import {deletecomment} from '@/network/Comment/Comment.js'
	export default{
		name:"SubBiuList",
		data(){
			return{
				showReplyId: '',
				loginId:null,
				ReplyLayer:null,
				CommentUrl:"http://127.0.0.1:8000/api/c/comments/"
			}
		},
		props:{
			comment:null,
		},
		components:{
			BiuBox
		},
		mounted() {
			if(localStorage.getItem('userid')){
				this.loginId = parseInt(localStorage.getItem('userid'))
			}
		},
		inject: ['reload'],
		methods:{
			toreply(reply){
				if(!this.showReplyId){
					this.showReplyId = reply.id
					this.ReplyLayer = reply
					console.log(this.ReplyLayer,"subcL")
				}
				else{
					this.showReplyId = ''
					this.ReplyLayer = null
				}
			},
			todelete(reply){
				deletecomment(this.CommentUrl,reply).then(res=>{
					this.reload() //局部刷新
				}).catch(err=>{
					console.log(err)
				})
			},
		}
	}
</script>

<style scoped="scoped">
	.sub{
		
	}
</style>
