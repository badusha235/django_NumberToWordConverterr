from django import forms




class NumberForm(forms.Form):
    number=forms.IntegerField(widget=forms.TextInput(attrs={'class':"form-control"}))
    # def clean(self):
    #     cleaned_data=super().clean()
    #     number=cleaned_data["number"]
         
    #     try:
            
    #         number=int(number)
    #         number==0
    #             # msg="invalid price"
    #             # self.add_error("price",msg)
    #     except:
    #         msg="invalid price"
    #         self.add_error("number",msg)
   
    
        