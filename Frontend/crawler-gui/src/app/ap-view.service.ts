import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApViewService {

  constructor() { }
  private currentViewSubject = new BehaviorSubject<string>('home');
  currentView$ = this.currentViewSubject.asObservable();

  setCurrentView(view: string) {
    this.currentViewSubject.next(view);
  }
}
