(function(t){function e(e){for(var r,a,i=e[0],c=e[1],l=e[2],d=0,p=[];d<i.length;d++)a=i[d],Object.prototype.hasOwnProperty.call(s,a)&&s[a]&&p.push(s[a][0]),s[a]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);u&&u(e);while(p.length)p.shift()();return o.push.apply(o,l||[]),n()}function n(){for(var t,e=0;e<o.length;e++){for(var n=o[e],r=!0,i=1;i<n.length;i++){var c=n[i];0!==s[c]&&(r=!1)}r&&(o.splice(e--,1),t=a(a.s=n[0]))}return t}var r={},s={app:0},o=[];function a(e){if(r[e])return r[e].exports;var n=r[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,a),n.l=!0,n.exports}a.m=t,a.c=r,a.d=function(t,e,n){a.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},a.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},a.t=function(t,e){if(1&e&&(t=a(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(a.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)a.d(n,r,function(e){return t[e]}.bind(null,r));return n},a.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return a.d(e,"a",e),e},a.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},a.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],c=i.push.bind(i);i.push=e,i=i.slice();for(var l=0;l<i.length;l++)e(i[l]);var u=c;o.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[t.showHistoryBool?n("div",[n("div",{attrs:{id:"admin-history-header"}},[n("h4",[t._v(t._s(t.currentUsername)+"'s feedback conversation")])]),n("div",{staticClass:"admin-history-container"},[n("div",{attrs:{id:"admin-conversation-linked-history"}},[n("div",{attrs:{id:"history-chat-panel"}},[n("ul",{staticClass:"collection with-header"},[n("li",{staticClass:"collection-header"},[n("button",{staticClass:"waves waves-light btn deep-purple darken-3",on:{click:function(e){t.showHistoryBool=!1}}},[t._v(" Back ")])]),n("li",{ref:"messageContainerScroll",staticClass:"collection-item custom-grey ",attrs:{id:"history-chat-container"}},[n("div",[t._l(t.conversationComputed,(function(t,e){return n("div",{key:e},["chatbot"==t.author?n("chat-bot-message",{attrs:{content:t.content}}):n("user-message",{attrs:{author:t.author,content:t.content}})],1)})),n("div",[n("div",{staticClass:"card teal darken-1"},[n("div",{staticClass:"card-content white-text"},[n("span",{staticClass:"card-title"},[t._v(t._s(t.currentUsername)+" found this conversation helpful")])])])])],2)])])])])]),n("div",{attrs:{id:"admin-history-header"}},[n("h4",[t._v("Problems and solution in details")]),n("h5",[t._v(t._s(t.currentUsername)+"'s problem")])]),n("div",{attrs:{id:"admin-history-content"}},[n("p",[t._v(t._s(t.currentProblem))])]),n("div",{attrs:{id:"admin-history-header"}},[n("h5",[t._v(t._s(t.currentUsername)+"'s solution")])]),n("div",{attrs:{id:"admin-history-header"}},[n("p",[t._v(t._s(t.currentSolution))])])]):n("div",[t.listIsEmptyComputed?n("div",{staticClass:"row",attrs:{id:"history-row"}},[t.startDelay?n("div",{staticClass:"col offset-s4 s4"},[t._m(1)]):t._e()]):n("div",{staticClass:"row",attrs:{id:"history-row"}},[n("div",{attrs:{id:"admin-panel-container"}},[n("table",[t._m(0),n("tbody",t._l(t.solutions,(function(e,r){return n("tr",{key:r},[n("td",{staticClass:"username-td"},[t._v(t._s(e.username))]),n("td",{staticClass:"problem-td"},[t._v(" "+t._s(e.problem.length>30?e.problem.substring(0,30)+"...":e.problem)+" ")]),n("td",{staticClass:"solution-td"},[t._v(" "+t._s(e.solution.length>30?e.solution.substring(0,30)+"...":e.solution)+" ")]),n("td",{staticClass:"details-td"},[n("a",{staticClass:"waves-effect waves-light btn btn-small",class:e.conversation.items&&e.conversation.items.length>0?"":"disabled",on:{click:function(e){return t.showHistory(r)}}},[t._v("see details")])]),n("td",{staticClass:"approve-td"},[n("label",[n("input",{directives:[{name:"model",rawName:"v-model",value:e.approved,expression:"data.approved"}],attrs:{type:"checkbox"},domProps:{checked:Array.isArray(e.approved)?t._i(e.approved,null)>-1:e.approved},on:{click:function(n){return t.sendApproveUpdate(e.solution_id,!e.approved)},change:function(n){var r=e.approved,s=n.target,o=!!s.checked;if(Array.isArray(r)){var a=null,i=t._i(r,a);s.checked?i<0&&t.$set(e,"approved",r.concat([a])):i>-1&&t.$set(e,"approved",r.slice(0,i).concat(r.slice(i+1)))}else t.$set(e,"approved",o)}}}),n("span",[t._v(t._s(e.approved?"Disapprove":" Approve"))])])])])})),0)])])])])])},o=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("thead",[n("tr",[n("th",[t._v("Username")]),n("th",[t._v("Problem")]),n("th",[t._v("Solution")]),n("th",[t._v("Details and Conversation")]),n("th",[t._v("Approve")])])])},function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"card deep-purple darken-3"},[n("div",{staticClass:"card-content white-text"},[n("span",{staticClass:"card-title"},[t._v("There is no new solution yet ! ")]),n("p",[t._v(" Wait for user publication to see and edit new solutions ! ")])])])}],a=(n("d81d"),n("96cf"),n("1da1")),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"user-message"},[n("div",{staticClass:"message-author"},[t._v(" "+t._s(t.author)+" ")]),n("div",{staticClass:"message-content"},[t._v(" "+t._s(t.content)+" ")])])},c=[],l={name:"UserMessage",props:{author:String,content:String}},u=l,d=n("2877"),p=Object(d["a"])(u,i,c,!1,null,"4345820b",null),v=p.exports,h=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"chatbot-message"},[n("div",{staticClass:"message-author"},[t._v(" chatbot ")]),n("div",{staticClass:"message-content",domProps:{innerHTML:t._s(t.content)}})])},m=[],f={name:"ChatBotMessage",props:{content:String}},_=f,b=Object(d["a"])(_,h,m,!1,null,"177e625c",null),y=b.exports,g=n("bc3a"),C=n.n(g),w={name:"Admin",components:{UserMessage:v,ChatBotMessage:y},data:function(){return{solutions:[],currentConversation:[],currentProblem:"",currentSolution:"",showHistoryBool:!1,currentUsername:"",startDelay:!1}},mounted:function(){var t=this;C.a.get("/admin-data").then((function(e){var n=e.data;null!==n&&n.length>0&&(t.solutions=n)})).catch((function(t){alert("Error, no internet connexion."),console.trace(t)})),setTimeout((function(){t.startDelay=!0}),3e3)},methods:{showHistory:function(t){this.selectCurrentConversation(t),this.currentUsername=this.solutions[t].username,this.currentProblem=this.solutions[t].problem,this.currentSolution=this.solutions[t].solution,this.showHistoryBool=!0},selectCurrentConversation:function(t){this.currentConversation=this.solutions[t].conversation.items},sendApproveUpdate:function(t,e){return Object(a["a"])(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:C.a.put("/admin-data/solution",{solution_id:t,approved:e},{headers:{"Content-Type":"application/json"}}).then((function(t){})).catch((function(t){alert("Error, no internet connexion."),console.trace(t)}));case 1:case"end":return n.stop()}}),n)})))()}},computed:{listIsEmptyComputed:function(){return 0===this.solutions.length},conversationComputed:function(){var t=this;return this.currentConversation.map((function(e){var n;return n="Q"===e.type?{author:t.currentUsername,content:e.text}:{author:"chatbot",content:e.text},n}))}}},k=w,x=(n("aa11"),Object(d["a"])(k,s,o,!1,null,null,null)),O=x.exports;r["a"].config.productionTip=!1,new r["a"]({render:function(t){return t(O)}}).$mount("#admin-app")},aa11:function(t,e,n){"use strict";n("fb4a")},fb4a:function(t,e,n){}});
//# sourceMappingURL=app.js.map