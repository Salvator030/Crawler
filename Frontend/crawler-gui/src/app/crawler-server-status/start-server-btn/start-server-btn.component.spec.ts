import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StartServerBtnComponent } from './start-server-btn.component';

describe('StartServerBtnComponent', () => {
  let component: StartServerBtnComponent;
  let fixture: ComponentFixture<StartServerBtnComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StartServerBtnComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StartServerBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
