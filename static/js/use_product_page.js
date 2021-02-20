var worksheet = new Vue({
    el: '#use_product_sheet',
    data: {
      use_product_sheet_data:{worksheet:null,squad:null,date:null,warehouse:null,discription:null},
      n:1,
      serial_number:null,
      products:null,
      warehouses:null,
      worksheets:null,
      message:'無 對應聯單資料',
    },
    created(){
        axios.get('/product_list/')
        .then(res => {
            this.products=res.data
        })
        .catch(err => {
            console.error(err); 
        })
    },
    methods:{
        new_products(){
            var n=this.n;
            var products=this.products;
            div=document.getElementById('productss_div')
            ele1 = document.createElement('input');
            ele1.onkeyup=function(){
                input = document.getElementById('code'+n).value
                e1=document.getElementById('label3'+n)
                e2=document.getElementById('label4'+n)
                e3=document.getElementById('product'+n)
                e1.innerHTML="材料:--"
                e2.innerHTML="單位:--"
                e3.value=null
                for (i = 0; i < products.length; i++) {
                  if(input==products[i].code){
                    e1.innerHTML="材料:"+products[i].name
                    e2.innerHTML="單位:"+products[i].unit
                    e3.value=products[i].id
                  }
                }
            }
            ele2 = document.createElement('input');
            ele3=document.createElement('input');
            ele3.type="hidden";
            btn=document.createElement('button');
            br=document.createElement('br');
            label1=document.createElement('label')
            label2=document.createElement('label')
            label3=document.createElement('label')
            label4=document.createElement('label')
            btn.innerHTML='取消';
            label1.innerHTML='料號:';
            label2.innerHTML='數量:';
            label3.innerHTML='材料:--';
            label4.innerHTML='單位:--';

            btn.onclick=function(){
                document.getElementById('code'+n).parentNode.removeChild(document.getElementById('code'+n))
                document.getElementById('amount'+n).parentNode.removeChild(document.getElementById('amount'+n))
                document.getElementById('cancel_btn'+n).parentNode.removeChild(document.getElementById('cancel_btn'+n))
                document.getElementById('br'+n).parentNode.removeChild(document.getElementById('br'+n))
                document.getElementById('label1'+n).parentNode.removeChild(document.getElementById('label1'+n))
                document.getElementById('label2'+n).parentNode.removeChild(document.getElementById('label2'+n))
                document.getElementById('label3'+n).parentNode.removeChild(document.getElementById('label3'+n))
                document.getElementById('label4'+n).parentNode.removeChild(document.getElementById('label4'+n))
                document.getElementById('product'+n).parentNode.removeChild(document.getElementById('product'+n))
            }
            ele1.name = 'code';
            ele1.id='code'+n;
            ele2.name = 'amount';
            ele2.id='amount'+n;
            ele2.type='number';
            ele3.name='product';
            ele3.id='product'+n;

            btn.id='cancel_btn'+n;
            br.id='br'+n;
            label1.id='label1'+n;
            label2.id='label2'+n;
            label3.id='label3'+n;
            label4.id='label4'+n;
            div.appendChild(label1);
            div.appendChild(ele1);
            div.appendChild(label3);
            div.appendChild(label4);
            div.appendChild(label2);
            div.appendChild(ele2);
            div.appendChild(btn);
            div.appendChild(br);
            div.appendChild(ele3);
            this.n++;
        },
        submit(){
            var use_product_sheet_id;
            axios.post('/use_product_sheet_list/',this.use_product_sheet_data)
            .then(res => {
                use_product_sheet_id=res.data['data']['id']
                product_elements=document.getElementsByName('product')
                amount_elements=document.getElementsByName('amount')
                var i;
                for (i = 0; i < product_elements.length; i++) {
                    console.log(product_elements[i].value)
                    console.log(amount_elements[i].value)
                    axios.post('/use_product_sheet_products_list/',{product:product_elements[i].value,
                    amount:amount_elements[i].value,
                    warehouse:this.use_product_sheet_data.warehouse,
                    use_product_sheet:use_product_sheet_id,
                    })
                    .then(res => {
                        console.log(res);
                    })
                    .catch(err => {
                        window.alert('批料輸入錯誤')
                    })
                }
                window.alert('完工單新增成功')

            })
            .catch(err => {
                window.alert('完工單新增錯誤')
            })
        },
        update_warehouse_worksheet(){
            axios.get('/get_squad_warehouses/'+this.use_product_sheet_data.squad)
            .then(res => {
                this.warehouses=res.data
                select=document.getElementById('warehouse')
                select.innerHTML='';
                for(i=0;i<this.warehouses.length;i++){
                    option=document.createElement('option')
                    option.value=this.warehouses[i].id
                    option.innerHTML=this.warehouses[i].name
                    select.appendChild(option)
                }
                select.value=null
            })
            axios.get('/get_squad_worksheet/'+this.use_product_sheet_data.squad)
            .then(res => {
               this.worksheets=res.data
            })
            
        },
        search_worksheets(){
            this.message="無 對應聯單號"
            this.use_product_sheet_data.worksheet=null
            for (i = 0; i < this.worksheets.length; i++) {
                if(this.serial_number==this.worksheets[i].serial_number){
                  this.message="有 對應聯單號"
                  this.use_product_sheet_data.worksheet=this.worksheets[i].id
                }
              }
        }
    }
})