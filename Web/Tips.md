# Tips

## 熟练使用IDE

### 代码重构——重命名

**功能：** 重命名代码符号的标识符，例如字段、本地变量、方法、命名空间、属性和类型。

**使用时机：** 想要安全地进行重命名（无需查找所有实例）并复制/粘贴新名称。

操作原因：复制和粘贴整个项目的新名称可能会导致错误。 此重构工具将准确地执行重命名操作。

方法：

1. 突出显示要重命名的项，或将文本光标置于其中：

   ![显示突出显示的代码的屏幕截图。](https://docs.microsoft.com/zh-cn/cpp/ide/refactoring/images/rename_highlight.png?view=msvc-160)

2. 接下来，执行以下操作之一：

   - 键盘
     - 按“Ctrl+R”，然后按“Ctrl+R”。 （请注意，键盘快捷方式可能因所选的配置文件而有所不同。）
   - 鼠标
     - 选择“编辑 > 重构 > 重命名”。
     - 右键单击代码并选择“重命名”。

3. 在弹出的“重命名”窗口中，输入所选项的新名称，并单击“预览”按钮。 如果需要扩大或缩小重命名的范围，请更改“搜索范围”。

   ![“重命名”对话框。](https://docs.microsoft.com/zh-cn/cpp/ide/refactoring/images/rename_dialog.png?view=msvc-160)

    提示

   可以通过检查“如果确认了所有引用，则跳过预览更改”来跳过预览。

4. 当出现“预览更改 - 重命名”窗口时，请确保正确进行所请求的更改。 使用窗口上半部分的复选框，启用或禁用任何项的重命名。

   ![重命名预览。](https://docs.microsoft.com/zh-cn/cpp/ide/refactoring/images/rename_preview.png?view=msvc-160)

5. 当一切都正常时，单击“应用”按钮，项将在源代码中重命名。

### 断点

合理放置断点可以较快判断出错的位置

在断点处可以看到变量的值

![](https://github.com/liukanshan1/WebStudy/blob/main/tips%20(1).jpg)

## 整理写过的代码

整理写过的代码可以减少重复造轮子的过程

![](https://github.com/liukanshan1/WebStudy/blob/main/tips%20(2).jpg)

在不需要参与生成的文件右键属性，在生成中排除选为“是”

