import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { provideHttpClient } from '@angular/common/http';
import { CrawlerServerStatusComponent } from './crawler-server-status/crawler-server-status.component';
import { CrawlerServerStatusService } from './crawler-server-status/crawler-server-status.service';
import { StartServerBtnComponent } from './crawler-server-status/start-server-btn/start-server-btn.component';
import {SocketIoModule,SocketIoConfig, Socket} from 'ngx-socket-io';
import { SOCKET_IO_CONFIG } from './socket-config';
import { SocketService } from './app-socket.service';
import { CrawlrBtnService } from './crawler-server-status/start-server-btn/start-crawlr-btn.service';


@NgModule({
  declarations: [
    AppComponent,
    CrawlerServerStatusComponent,
    StartServerBtnComponent
   ],
  imports: [
    BrowserModule,
    SocketIoModule.forRoot(SOCKET_IO_CONFIG) 
  ],
  providers: [
    provideHttpClient(),  // Ersetze HttpClientModule durch provideHttpClient(),
    CrawlerServerStatusService,
    CrawlrBtnService,
    SocketService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
