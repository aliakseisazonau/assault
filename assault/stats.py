from typing import List, Dict

class Results:
    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = requests

    def slowest(self) -> float:
        """
        Returns the slowest request's completion time
    
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.slowest()
        6.1
        """  
        pass
    
    def fastest(self) -> float:
        """
        Returns the fastest request's completion time
    
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.fastest()
        1.04
        """
        pass
    
    def average_time(self) -> float:
        """
        Returns the average request completion time
    
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.average_time()
        9.846666667
        """
        pass
    
    def Successful_requests(self) -> int:
        """
        Returns the number of successful requests
    
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.successful_requests()
        2
        """
        pass


