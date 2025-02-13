import { Component } from '@angular/core';
import { CrawlerServerStatusComponent } from './crawler-server-status/crawler-server-status.component';
import { StartServerBtnComponent } from './crawler-server-status/start-server-btn/start-server-btn.component';
import { HeaderComponent } from './header/header.component';
import { ApViewService } from './ap-view.service';
import { CommonModule } from '@angular/common';
import { ArticlesComponent } from './articles/articles.component';
import { ResizeListenerComponent } from './resize-listener/resize-listener.component';

@Component({
  selector: 'app-root',
  imports: [CrawlerServerStatusComponent, HeaderComponent,CommonModule,ArticlesComponent, ResizeListenerComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})

export class AppComponent {
  constructor(private viewService: ApViewService ){}
  title = 'crawler-gui';
  currentView: string= "home"

  ngOnInit() {
    this.viewService.currentView$.subscribe(view => {
      this.currentView = view;
    });
  }
}
 