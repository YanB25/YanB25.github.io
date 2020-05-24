---
published: true
categories: Assignment
date: '2020-05-24 19:18:00 +0800'
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
