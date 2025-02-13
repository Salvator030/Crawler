import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { provideHttpClient } from '@angular/common/http';
import { CrawlerServerStatusComponent } from './body/crawler-server-status/crawler-server-status.component';
import { CrawlerServerStatusService } from './body/crawler-server-status/crawler-server-status.service';
import { StartServerBtnComponent } from './body/crawler-server-status/start-server-btn/start-server-btn.component';
import {SocketIoModule,SocketIoConfig, Socket} from 'ngx-socket-io';
import { SOCKET_IO_CONFIG } from './socket-config';
import { SocketService } from './app-socket.service';
import { CrawlrBtnService } from './body/crawler-server-status/start-server-btn/start-crawlr-btn.service';
import { HeaderComponent } from './header/header.component';
import { ApViewService } from './ap-view.service';
import { CommonModule } from '@angular/common';
import { ArticlesComponent } from './body/articles/articles.component';
import { ArticlesService } from './body/articles/articles.service';
import { ArticleItemComponent } from './body/articles/article-item/article-item.component';
import { ResizeListenerComponent } from './resize-listener/resize-listener.component';
import { ArticleQueryComponent } from './body/articles/article-query/article-query.component';


@NgModule({
  declarations: [
    AppComponent,
    CrawlerServerStatusComponent,
    StartServerBtnComponent,
    HeaderComponent,
    ArticlesComponent,
    ArticleItemComponent,
    ResizeListenerComponent,
    ArticleQueryComponent
   ], 
  imports: [
    BrowserModule,
    CommonModule,
    SocketIoModule.forRoot(SOCKET_IO_CONFIG) 
  ],
  providers: [
    provideHttpClient(),  // Ersetze HttpClientModule durch provideHttpClient(),
    CrawlerServerStatusService,
    CrawlrBtnService,
    SocketService,
    ApViewService,
    ArticlesService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
