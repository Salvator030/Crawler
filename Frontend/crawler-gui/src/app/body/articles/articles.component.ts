import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ArticlesService } from './articles.service';
import { ArticleItemComponent } from './article-item/article-item.component';
import { ArticleQueryComponent } from './article-query/article-query.component';

@Component({
  standalone: true,
  selector: 'app-articles',
  imports: [CommonModule,ArticleItemComponent,ArticleQueryComponent],
  templateUrl: './articles.component.html',
  styleUrl: './articles.component.scss'
})
export class ArticlesComponent {

  articles: [] = []

  constructor(){}

  
  updateArticles(articles: []){
    this.articles = articles}

    handelOnClickNewSeachBtn(){
      this.articles = []
    }  

}
