import diffusers.pipelines as p


def is_sd15(model):
    if model is None:
        return False
    if hasattr(model, '__name__'):
        return model.__name__ == p.StableDiffusionPipeline.__name__ or model.__name__ == p.StableDiffusionImg2ImgPipeline.__name__ or model.__name__ == p.StableDiffusionInpaintPipeline.__name__
    return isinstance(model, p.StableDiffusionPipeline) or isinstance(model, p.StableDiffusionImg2ImgPipeline) or isinstance(model, p.StableDiffusionInpaintPipeline)


def is_sdxl(model):
    if model is None:
        return False
    if hasattr(model, '__name__'):
        return model.__name__ == p.StableDiffusionXLPipeline.__name__ or model.__name__ == p.StableDiffusionXLImg2ImgPipeline.__name__ or model.__name__ == p.StableDiffusionXLInpaintPipeline.__name__
    return isinstance(model, p.StableDiffusionXLPipeline) or isinstance(model, p.StableDiffusionXLImg2ImgPipeline) or isinstance(model, p.StableDiffusionXLInpaintPipeline)

def is_f1(model):
    if model is None:
        return False
    if hasattr(model, '__name__'):
        return model.__name__ == p.FluxPipeline.__name__ or model.__name__ == p.FluxImg2ImgPipeline.__name__ or model.__name__ == p.FluxInpaintPipeline.__name__
    return isinstance(model, p.FluxPipeline) or isinstance(model, p.FluxImg2ImgPipeline) or isinstance(model, p.FluxInpaintPipeline)

def is_sd3(model):
    if model is None:
        return False
    if hasattr(model, '__name__'):
        return model.__name__ == p.StableDiffusion3Pipeline.__name__ or model.__name__ == p.StableDiffusion3Img2ImgPipeline.__name__ or model.__name__ == p.StableDiffusion3InpaintPipeline.__name__
    return isinstance(model, p.StableDiffusion3Pipeline) or isinstance(model, p.StableDiffusion3Img2ImgPipeline) or isinstance(model, p.StableDiffusion3InpaintPipeline)
