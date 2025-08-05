<template>
	<div class="container m-auto">
		<AuthorInfo />
		<AbstractComp />
		<CodeBox :json="json1" />
		<CodeBox :json="json2" />
		<CitationComp />
	</div>
</template>

<script setup>
import AuthorInfo from './components/AuthorInfo.vue'
import AbstractComp from './components/AbstractComp.vue'
import CodeBox from './components/CodeBox.vue'
import CitationComp from './components/CitationComp.vue'
import json1 from './json/videoData1.json'
import json2 from './json/videoData2.json'
</script>

<style scoped>
.container {
	width: 96%;
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #212529;
}
@media (min-width: 576px) {
	.container {
		max-width: 540px;
	}
}
@media (min-width: 768px) {
	.container {
		
		max-width: 720px;
	}
}
@media (min-width: 992px) {
	.container {
		max-width: 960px;
	}
}
</style>
