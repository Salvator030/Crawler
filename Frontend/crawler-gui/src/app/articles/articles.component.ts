import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ArticlesService } from './articles.service';
import { ArticleItemComponent } from './article-item/article-item.component';

@Component({
  selector: 'app-articles',
  imports: [CommonModule,ArticleItemComponent],
  templateUrl: './articles.component.html',
  styleUrl: './articles.component.scss'
})
export class ArticlesComponent {

  articles: [] = []

  constructor(private articlesService: ArticlesService){}

  ngOnInit(){
    this.articlesService.getAllArticles().subscribe({
      next: (response: any) => {
        this.articles = response.msg
        console.log(this.articles)
      }
    })
  }

}
