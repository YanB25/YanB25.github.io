---
published: false
categories: Assignment
date: '2020-05-24 19:18:00 +0800'
---
## Bug汇总

这篇blog会长期更新。我会在其中更新一些让我印象深刻的bug。

### On Eval Order

``` c++
auto ctx = std::make_unique<Context>();
AsyncFunction(ctx->a, ctx->b, new CallBack(ctx.release());
```

where `CallBack` is defined as below. It automatically does the cleanup when `AsyncFunction` finishes its job (and causes `CallBack` destructing).

``` c++
class CallBack
{
public:
  CallBack(std::unique_ptr<Context> ctx) : ctx_(ctx)
  {
  }
  ~CallBack()
  {
    ctx_->Free();
  }
private:
  std::unique_ptr<Context> ctx_;
}
```