import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-article-item',
  imports: [],
  templateUrl: './article-item.component.html',
  styleUrl: './article-item.component.scss'
})
export class ArticleItemComponent {

  @Input()
  obj: any;
  
  headline: String = "";
  subHeadline: String = "";
  description: String ="";
  content: String = "";
  date: String = "";
  publisher: String = "";
  writer: String = "";
  id: Number = 0;


  ngOnInit(): void{
    this.headline = this.obj.headline;
    this.subHeadline = this.obj.subHeadline;
    this.description = this.obj.description;
    this.content = this.obj.last_content;
    this.date = this. obj.data
    this.publisher = this. obj.publisher;
    this.writer = this.obj.writer;
    this.id = this.obj.id;
  }
}
