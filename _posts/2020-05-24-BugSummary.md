---
published: true
categories: Assignment
date: '2020-05-24 19:18:00 +0800'
title: Bug Summary
---

这篇blog会长期更新。我会在其中更新一些让我印象深刻的bug。

## About Eval Order

Order of evaluation of function arguments is *unspecific*. See [here](https://en.cppreference.com/w/cpp/language/eval_order).

### Background

`AsyncFunction` may take unpredictable time to finish its job, after which the callback argument is called.


``` c++
auto ctx = std::make_unique<Context>();
AsyncFunction(ctx->a, ctx->b, new Callback(ctx.release());
```

where `CallBack` is defined as below. It automatically does the cleanup when `AsyncFunction` finishes its job (and causes `CallBack` destructing).

``` c++
class Callback
{
public:
  Callback(std::unique_ptr<Context> ctx) : ctx_(ctx)
  {
  }
  void Run()
  {
    std::cout << "Running the Callback here..." << std::endl;
    // Do a lot of jobs
    ctx_->Free();
  }
private:
  std::unique_ptr<Context> ctx_;
}
```

### Symptom

Program crashes @ `AsyncFunction`. That's all gdb can provide.

### Bug & Solution

`ctx.release()` may be evaluated *before* `ctx->a`, which is referencing an invalidated pointer.

```c++
// A solution
AsyncFunction(ctx->a, ctx->b, new Callback(ctx.get());
ctx.release();
```

## Race Condition

Race condition may be very difficult to detect. Most RC drive the program into an unexpected state, and the root cause (bug) may locate far away when user find a wrong result.

### Background

``` c++
std::atomic<bool> stop_{true};
std::thread loop([] {
  while (!stop_.load())
  {
    std::cout << "I am working" << std::endl;
    sleep(1);
  }
});
stop_.store(false);
```

### Symptom

We expect to see an output every second. However, *sometimes* users may find there's no output at all.

### Bug & Solution

Solution: just put `stop_.store(true)` before spawning the thread.

In a complex program where each functionality is layered, this kind of bug is difficult to detect and locate.
