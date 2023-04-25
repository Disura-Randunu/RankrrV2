import { TestBed } from '@angular/core/testing';

import { RankerService } from './ranker.service';

describe('RankerService', () => {
  let service: RankerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RankerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
