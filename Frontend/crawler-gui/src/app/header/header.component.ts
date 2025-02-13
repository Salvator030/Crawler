import { Component } from '@angular/core';
import { ApViewService } from '../ap-view.service';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-header',
  imports: [CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  constructor(private viewService: ApViewService) {}

  handelOnClickHomeBtn(){
    this.viewService.setCurrentView("home");
  }

  handelOnClickArticlesBtn(){
    this.viewService.setCurrentView("articles");
  }
  
}
