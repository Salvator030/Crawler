import { TestBed } from '@angular/core/testing';

import { ApViewService } from './ap-view.service';

describe('ApViewService', () => {
  let service: ApViewService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApViewService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
