var control_panel = new Vue({
    el: '#control_panel',
    data: {
      product_page:{formData:new FormData(),name:null,code:null,unit:null,create_form_show:false,show:false},
      product_list:null,
      warehouse_page:{name:null,location:null,squad:null,create_form_show:false,show:false},
      warehouse_list:[],
      squad_page:{name:null,create_form_show:false,show:false},
      squad_list:[]
    },

    methods:{
        fileChange(e){
            this.product_page.formData.append('photo',e.target.files[0])
        },
        show_product_page:function(){
            this.all_hide()
            this.product_page.show=true
            axios.get('/product_list/')
            .then(res => {
                console.log(res)
                this.product_list=res.data
            })
            .catch(err => {
                console.error(err); 
            })
        },
        create_product:function(){
            
            this.product_page.formData.append('name',this.product_page.name)
            this.product_page.formData.append('code',this.product_page.code)
            this.product_page.formData.append('unit',this.product_page.unit)
            axios.post('/product_list/',this.product_page.formData)
            .then(res => {
                console.log(res)
                this.product_page.formData.delete('name')
                this.product_page.formData.delete('code')
                this.product_page.formData.delete('unit')
                this.product_page.formData.delete('photo')
            })
            .catch(err => {
                console.error(err); 
            })
        },
        show_squad_page(){
            this.all_hide()
            this.squad_page.show=true
            axios.get('/squad_list/')
            .then(res => {
                console.log(res)
                this.squad_list=res.data
            })
            .catch(err => {
                console.error(err); 
            })
        },
        create_squad:function(){
            
            axios.post('/squad_list/',{name:this.squad_page.name})
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.error(err); 
            })
        },
        squad_detail(id){
            el=document.getElementById("squad_workers"+id)
            if(el.style.display=='none'){
                el.style.display='block'
            }else{
                el.style.display='none'
            }
        },
        squad_update_show(id){
            el=document.getElementById("squad_edit"+id)
            if(el.style.display=='none'){
                el.style.display='block'
            }else{
                el.style.display='none'
            }
        },
        squad_update(id){
                axios.put("/squad_detail/"+id,{name:document.getElementById("squad_name"+id).value })
                .then(res => {
                    location.reload();
                })
                .catch(err => {
                    console.error(err); 
                })
            
        },
        squad_delete(id){
            result=window.confirm('確定刪除?')
            if( result ){
                axios.delete("/squad_detail/"+id)
                .then(res => {
                    console.log(res)
                    location.reload();
                })
                .catch(err => {
                    console.error(err); 
                })
            }
        },
        show_warehouse_page:function(){
            this.all_hide()
            this.warehouse_page.show=true
        },
        create_warehouse:function(){
            axios.post('/warehouse_list/',{name:this.warehouse_page.name,location:this.warehouse_page.location,squad:this.warehouse_page.squad})
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.error(err); 
            })
        },
        warehouse_update_show(id){
            el=document.getElementById("warehouse_edit"+id)
            if(el.style.display=='none'){
                el.style.display='block'
            }else{
                el.style.display='none'
            }
        },
        warehouse_update(id){
                axios.put("/warehouse_detail/"+id,{name:document.getElementById("warehouse_name"+id).value,
                                                    location:document.getElementById("warehouse_location"+id).value,
                                                    squad:document.getElementById("warehouse_squad"+id).value })
                .then(res => {
                    console.log(res)
                    location.reload();
                })
                .catch(err => {
                    console.error(err); 
                })
            
        },
        warehouse_delete(id){
            result=window.confirm('確定刪除?')
            if( result ){
                axios.delete("/warehouse_detail/"+id)
                .then(res => {
                    console.log(res)
                    location.reload();
                })
                .catch(err => {
                    console.error(err); 
                })
            }
        },
        
        all_hide:function(){
            this.product_page.show=false
            this.warehouse_page.show=false
            this.squad_page.show=false
        },
    },
  })