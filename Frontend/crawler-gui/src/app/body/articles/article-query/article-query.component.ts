import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-article-query',
  imports:[CommonModule , FormsModule],
  templateUrl: './article-query.component.html',
  styleUrl: './article-query.component.scss'
})
export class ArticleQueryComponent {

  checkTsp: boolean = false;
  checkSpiegel: boolean = false;
  date: String =""

}
