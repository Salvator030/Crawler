import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResizeListenerComponent } from './resize-listener.component';

describe('ResizeListenerComponent', () => {
  let component: ResizeListenerComponent;
  let fixture: ComponentFixture<ResizeListenerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ResizeListenerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ResizeListenerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
