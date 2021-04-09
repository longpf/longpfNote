* **plist读写操作如何进行锁管理**
	
	* `- (BOOL)writeToFile:(NSString *)path atomically:(BOOL)useAuxiliaryFile;` useAuxiliaryFile如果为yes则先写入临时文件,再rename到path. 为no的话,直接写入path.多个线程可以同时写入,可能导入最后的数据是脏数据,
	* `dispatch_barrier_async`可以采用这个设计,并在内存保留一份plist缓存文件, 防止频繁读取文件,需要考虑缓存超出给定大小的情况(FIFO,LRU),还有收到内存警告的情况

* **NSNotification实现逻辑，子线程中给主线程发送通知，主线程是否会处理通知**
	* 看子线程runloop是否开启,没run的情况发送不了
	* 源码说明:[https://juejin.cn/post/6844904082516213768#QlZ7o](https://juejin.cn/post/6844904082516213768#QlZ7o)
	* 注册通知:
		* case1:存在name的情况. 1,先从NCTable中找到named表, 这个表中存储了含有name的通知. 2,以name为key,从这个表中找value,value是个map. 3,以object为key,从map中找到obs,**obs对象是个链表,每个节点存observer和SEL**,然后把新创建的obs节点存上去
		* case2:以object为key,从NCTable中的nameless字典中取value,value是obs链表
		* case3:从NCTable中的取wildcard链表(obs链表)
		* `addObserverForName:object:queue:usingBlock`这个是生成一个劣势obsever调用不带block的方法
	* 存储是以name和object为维度的，即判定是不是同一个通知要从name和object区分，如果他们都相同则认为是同一个通知.如果name相同,object不同,那post的时候收不到通知
	* 发送通知: 1, 生成notification对象,从named,nameless,wildcard表中找到对应obs节点,然后`[o->observer performSelector:o->selector withObject:notification]`
	* 发送的时候,是同步发送,遍历所有列表,注册多次,就会有多个结点,通知就会响应多次
	
* **编译器怎么检测#import和#include导入多次的问题，三方库导入时如何设置""和<>**
	* import不回重复导入,可能采用#ifndef, include会报重复导入,
	* 双引号用户本地文件需要指明相对路径,尖括号是全局引用,路径由编译器提供.
	* cocoapod导入的文件会自动加到header search path