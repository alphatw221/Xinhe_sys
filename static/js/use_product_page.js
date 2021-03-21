var worksheet = new Vue({
    el: '#use_product_sheet',
    data: {
      use_product_sheet_data:{serial_number:null,worksheet:null,status:null,squad:null,date:null,warehouse:null,discription:null,point:null,project:null},
      n:1,
      squad:'',
      project:'',
      warehouses:[],
      message:'無 對應聯單資料',
    },
    methods:{
        new_products(){
            var n=this.n;
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
                axios.get('/get_product_with_code/',{params:{code:input}})
                .then(res => {
                    e1.innerHTML="材料:"+res.data.name
                    e2.innerHTML="單位:"+res.data.unit
                    e3.value=res.data.id
                })
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
            btn.className = 'btn btn-danger';
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
            product_elements=document.getElementsByName('product')
            amount_elements=document.getElementsByName('amount')
            data=[]
                for (i = 0; i < product_elements.length; i++) {
                    data.push({product:product_elements[i].value,
                        amount:amount_elements[i].value,
                        warehouse:this.use_product_sheet_data.warehouse
                        })
                }
            axios.post('/use_product_sheet_list/',{use_product_sheet:this.use_product_sheet_data,use_product_sheet_productss:data})
            .then(res => {
                window.alert(res.data['message'])
                
            })
            .catch(err => {
                window.alert('領貨單新增錯誤')
            })
        },
        search_worksheets(){
            axios.get('/get_worksheet_with_serial_number/',{params:{serial_number:this.use_product_sheet_data.serial_number}})
            .then(res => {
                if(res.data){
                    this.message='有 對應聯單資料'
                }else{
                    this.message='無 對應聯單資料'
                }
                this.use_product_sheet_data.squad=res.data.squad_id
                this.squad=res.data.squad_name
                this.warehouses=res.data.warehouses
                this.use_product_sheet_data.point=res.data.point
                this.use_product_sheet_data.worksheet=res.data.worksheet_id
                this.use_product_sheet_data.project=res.data.project_id
                this.project=res.data.project_name
            })
        }
    }
})