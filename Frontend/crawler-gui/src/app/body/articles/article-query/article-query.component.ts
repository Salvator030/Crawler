import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ArticlesService } from '../articles.service';

@Component({
  selector: 'app-article-query',
  imports:[CommonModule , FormsModule],
  templateUrl: './article-query.component.html',
  styleUrl: './article-query.component.scss'
})
export class ArticleQueryComponent {

  constructor(private articleService:ArticlesService){}
  


  @Output()
  newArticles = new EventEmitter<[]>

  publishers = [{name:"tsp", checked:false},{name:"spiegel", checked: false}
  ];
  date: String ="";
  isFetch: boolean =false;
  isResultEmpty = false;

  handelClickOnBtn(){
    

     this.submit();
    
  }

  submit(){
   
    if(this.publishers.filter(publisher => publisher.checked).length == 0 && this.date == ""){
      this.articleService.getAllArticles().subscribe({
        next: (respone: any) => {
        respone.msg
         this.newArticles.emit(respone.msg)
      }})
    }
    else{
      this.articleService.getArticlesBy(this.getJsonQuery()).subscribe(response => {
        if(response.msg != 0 ){
          this.isResultEmpty = true;
        this.newArticles.emit(response.msg);
         this.isResultEmpty = false;}
       
        else{
          this.isResultEmpty = true;
        }
    }, error => {
      console.error('Error:', error);
    });
    }
    
  
  }

  getJsonQuery(){
   
    const selectedPublishers = this.publishers.filter(publisher => publisher.checked);
    const publischersName = selectedPublishers.map(publisher => publisher.name);
    const json = {publisher: publischersName, date: this.date}
    return json
  }

}
